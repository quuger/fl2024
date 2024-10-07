#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <queue>

namespace machine {
    struct Node {
        int id;
        bool is_end;
        std::map<int, std::set<int>> adjacent;
    };

    struct Machine {
        int n;
        int m;
        std::set<int> start_nodes;
        std::set<int> end_nodes;
        std::vector <Node> nodes;
        std::vector<bool> deleted_nodes;

        static bool read_line(std::set<int> &data);
        void read();
        void write();

        void dfs(const Node &v, const std::vector <Node> &graph, std::vector<bool> &used);
        void delete_states(const std::set<int> &start, const std::vector <Node> &graph);

        void simplify();
        void convert_to_dfa(Machine &dfa);

        void build_dfa(std::vector<int> &components, int component_count);
        std::vector<std::vector<bool>> build_matrix(std::vector<Node> &reverse_nodes);
        std::vector<Node> build_reverse_graph();
        void minimize();

        friend bool operator==(Machine &lhs, Machine &rhs);

        bool is_universal();
    };

    struct Checker {
        Machine &lhs;
        Machine &rhs;

        std::vector<bool> used;
        std::vector<int> isomorphic;

        bool dfs(Node &u, Node &v) {
            used[u.id] = true;
            if (u.is_end != v.is_end) {
                return false;
            }
            isomorphic[u.id] = v.id;
            bool answer = true;
            for (auto [symbol, st]: u.adjacent) {
                if (st.empty() != v.adjacent[symbol].empty()) {
                    return false;
                }
                int q = *st.begin();
                int s = *v.adjacent[symbol].begin();
                answer &= (used[q] ? s == isomorphic[q] : dfs(lhs.nodes[q], rhs.nodes[s]));
            }
            return answer;
        }

        operator bool() {
            if (lhs.n != rhs.n || lhs.m != rhs.m) {
                return false;
            }
            used.resize(lhs.n, false);
            isomorphic.resize(lhs.n, -1);
            return dfs(lhs.nodes[*lhs.start_nodes.begin()], rhs.nodes[*rhs.start_nodes.begin()]);
        }
    };

    bool Machine::read_line(std::set<int> &data) {
        std::string line;
        std::getline(std::cin, line);
        std::stringstream ss(line);
        for (int id; ss >> id;) {
            data.insert(id);
        }
        return !data.empty();
    }

    void Machine::read() {
        std::cin >> n >> m;
        std::cin.ignore();
        read_line(start_nodes);
        read_line(end_nodes);

        nodes.resize(n);

        for (auto i: end_nodes) {
            nodes[i].is_end = true;
        }
        for (std::vector<int> data(3); std::cin >> data[0] >> data[1] >> data[2];) {
            nodes[data[0]].adjacent[data[1]].insert(data[2]);
        }
    }

    void Machine::write() {
        std::cout << n << '\n' << m << '\n' << 0 << '\n'; // the starting node is always 0
        for (auto it = end_nodes.begin(); it != end_nodes.end();) {
            std::cout << *it << (++it != end_nodes.end() ? " " : "");
        }
        std::cout << '\n';
        for (const auto& node: nodes) {
            for (auto [symbol, other]: node.adjacent) {
                std::cout << node.id << ' ' << symbol << ' ' << *other.begin() << '\n';
            }
        }
    }

    void Machine::convert_to_dfa(Machine &dfa) {
        std::map<std::set<int>, int> nfa_nodes_to_dfa_node;
        std::map<int, std::set<int>> dfa_node_to_nfa_nodes;

        int current_id = 0;

        nfa_nodes_to_dfa_node[start_nodes] = current_id;
        dfa_node_to_nfa_nodes[current_id] = start_nodes;

        while (current_id < nfa_nodes_to_dfa_node.size()) {
            dfa.nodes.push_back({current_id, false});

            for (auto id: dfa_node_to_nfa_nodes[current_id]) {
                for (int symbol = 0; symbol < m; ++symbol) {
                    for (auto item: nodes[id].adjacent[symbol]) {
                        // break the DFA invariant: don't know the adjacent id
                        dfa.nodes[current_id].adjacent[symbol].insert(item);
                    }
                }
            }

            for (auto &[symbol, node]: dfa.nodes[current_id].adjacent) {
                if (nfa_nodes_to_dfa_node.find(node) == nfa_nodes_to_dfa_node.end()) {
                    auto id = nfa_nodes_to_dfa_node.size();
                    nfa_nodes_to_dfa_node[node] = id;
                    dfa_node_to_nfa_nodes[id] = node;
                }
                node = {nfa_nodes_to_dfa_node[node]}; // fix the DFA invariant
            }

            bool has_end_node = false;
            for (auto id: dfa_node_to_nfa_nodes[current_id]) {
                has_end_node |= nodes[id].is_end;
            }
            if (has_end_node) {
                dfa.end_nodes.insert(current_id);
                dfa.nodes[current_id].is_end = true;
            }

            ++current_id;
        }
        dfa.m = m;
        dfa.n = dfa.nodes.size();
        dfa.start_nodes = {0};
        dfa.simplify();
    }

    void Machine::dfs(const Node &v, const std::vector <Node> &graph, std::vector<bool> &used) {
        used[v.id] = true;
        for (const auto &[symbol, nodes_id]: v.adjacent) {
            for (const auto id: nodes_id) {
                if (!used[id]) {
                    dfs(graph[id], graph, used);
                }
            }
        }
    }

    void Machine::simplify() {
        delete_states(start_nodes, nodes); // unreachable

        auto reversed_nodes = build_reverse_graph();
        delete_states(end_nodes, reversed_nodes); // dead

        n = nodes.size();
    }

    void Machine::delete_states(const std::set<int> &start, const std::vector <Node> &graph) {
        std::vector<bool> used(n, false);
        for (auto id: start) {
            dfs(graph[id], graph, used);
        }
        for (int id = 0; id < n; ++id) {
            if (!used[id]) {
                deleted_nodes[id] = true;
            }
        }
    }

    std::vector<Node> Machine::build_reverse_graph() {
        std::vector <Node> reversed_nodes(nodes.size());
        for (auto &node: nodes) {
            for (auto &[symbol, other]: node.adjacent) {
                reversed_nodes[*other.begin()].adjacent[symbol].insert(node.id);
            }
        }
        for (int i = 0; i < reversed_nodes.size(); ++i) {
            reversed_nodes[i].id = i;
        }
        return reversed_nodes;
    }

    std::vector<std::vector<bool>> Machine::build_matrix(std::vector<Node> &reverse_nodes) {
        std::queue<std::pair<int, int>> queue;
        std::vector<std::vector<bool>> marked(n, std::vector<bool> (n));

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nodes[i].is_end != nodes[j].is_end) {
                    marked[i][j] = marked[j][i] = true;
                    queue.emplace(i, j);
                }
            }
        }

        while (!queue.empty()) {
            auto [u, v] = queue.front();
            queue.pop();
            for (int symbol = 0; symbol < m; ++symbol) {
                for (int a: reverse_nodes[u].adjacent[symbol]) {
                    for (int b: reverse_nodes[v].adjacent[symbol]) {
                        if (!marked[a][b]) {
                            marked[a][b] = marked[b][a] = true;
                            queue.emplace(a, b);
                        }
                    }
                }
            }
        }

        return marked;
    }

    void Machine::build_dfa(std::vector<int> &components, int component_count) {
        std::vector<Node> new_nodes(component_count);
        std::set<int> new_end_nodes;
        for (int i = 0; i < n; ++i) {
            for (int symbol = 0; symbol < m; ++symbol) {
                new_nodes[components[i]].adjacent[symbol].insert(nodes[i].adjacent[symbol].begin(),
                                                                 nodes[i].adjacent[symbol].end());
            }
            new_nodes[components[i]].is_end |= nodes[i].is_end;
        }
        for (const auto& node: new_nodes) {
            if (node.is_end) {
                new_end_nodes.insert(node.id);
            }
        }

        n = component_count;
        nodes = std::move(new_nodes);
        start_nodes = {components[*start_nodes.begin()]};
        end_nodes = std::move(new_end_nodes);
    }

    void Machine::minimize() {
        simplify();

        auto reversed_nodes = build_reverse_graph();
        std::vector<std::vector<bool>> marked = build_matrix(reversed_nodes);

        std::vector<int> components(n);
        for (int i = 0; i < n; ++i) {
            components[i] = (!marked[0][i] ? 0 : -1);
        }

        int component_count = 0;
        for (int i = 0; i < n; ++i) {
            if (components[i] != -1) {
                continue;
            }
            components[i] = ++component_count;
            for (int j = i + 1; j < n; ++j) {
                if (!marked[i][j]) {
                    components[j] = component_count;
                }
            }
        }
        build_dfa(components, component_count);
    }

    bool operator==(Machine &lhs, Machine &rhs) {
        return Checker(lhs, rhs);
    }

    bool Machine::is_universal() {
        minimize();
        bool answer = n == 1;
        for (int symbol = 0; symbol < m; ++symbol) {
            answer &= nodes[0].adjacent[symbol].find(0) != nodes[0].adjacent[symbol].end();
        }
        return answer;
    }

    void solve() {
        Machine nfa, dfa;
        nfa.read();
        nfa.convert_to_dfa(dfa);
        dfa.write();
    }

    void solve_minimize() {
        Machine dfa;
        dfa.read();
        dfa.write();
    }

    void solve_equivalent() {
        Machine dfa1, dfa2;
        dfa1.read();
        dfa2.read();
        std::cout << std::boolalpha << (dfa1 == dfa2);
    }

    void solve_universal() {
        Machine dfa;
        dfa.read();
        std::cout << std::boolalpha << dfa.is_universal();
    }
}
