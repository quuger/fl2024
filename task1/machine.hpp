#ifndef MACHINE_HPP_
#define MACHINE_HPP_

#include <vector>
#include <set>
#include <map>

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

        Checker(Machine &lhs_, Machine &rhs_) : lhs(lhs_), rhs(rhs_) {}

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

    void solve();
    void solve_minimize();
    void solve_equivalent();
    void solve_universal();
}

#endif // MACHINE_HPP_
