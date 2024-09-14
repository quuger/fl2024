#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <sstream>
#include <set>

namespace machine {
    struct Node {
        int id;
        bool is_end;
        std::map<int, std::set<int>> adjacent;
    };

    struct Node_Signature {
        std::map<int, std::set<int>> previous;
        std::map<int, int> next;
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

        void convert_to_dfa(Machine &dfa);

        void simplify();

        void delete_states(const std::set<int> &start, const std::vector <Node> &graph);
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
        for (auto node: nodes) {
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

        std::vector <Node> reversed_nodes(nodes.size());
        for (auto &node: nodes) {
            for (auto &[symbol, other]: node.adjacent) {
                reversed_nodes[*other.begin()].adjacent[symbol].insert(node.id);
            }
        }
        for (int i = 0; i < reversed_nodes.size(); ++i) {
            reversed_nodes[i].id = i;
        }
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

    void solve() {
        Machine nfa, dfa;
        nfa.read();
        nfa.convert_to_dfa(dfa);
        dfa.write();
    }
}

int main() {
    machine::solve();
    return 0;
}
