#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        from collections import defaultdict

        email_to_name = {}
        graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                graph[account[1]].add(email)
                graph[email].add(account[1])

        visited = set()
        merged_accounts = []

        def dfs(email):
            stack = [email]
            component = []
            while stack:
                curr_email = stack.pop()
                if curr_email not in visited:
                    visited.add(curr_email)
                    component.append(curr_email)
                    for neighbor in graph[curr_email]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return component

        for email in email_to_name:
            if email not in visited:
                component = dfs(email)
                merged_accounts.append([email_to_name[email]] + sorted(component))

        return merged_accounts
        
# @lc code=end

