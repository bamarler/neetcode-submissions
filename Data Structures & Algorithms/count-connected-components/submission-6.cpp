class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);

        for(vector<int>& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        vector<int> colors(n, 0);
        int count = 0;

        for(int start = 0; start < n; start++) {
            if (colors[start] != 0) {
                continue;
            }
            count += 1;
            vector<int> stack;
            stack.push_back(start);
            colors[start] = 1;
            while (stack.size() > 0) {
                int node = stack.back();
                bool pushed = false;
                for (auto& neighbor : adj[node]) {
                    if (colors[neighbor] == 0) {
                        colors[neighbor] = 1;
                        stack.push_back(neighbor);
                        pushed = true;
                        break;         
                    }
                }
                if (!pushed) {
                    colors[node] = 2;
                    stack.pop_back();
                }
            }   
        }

        return count;
    }
};
