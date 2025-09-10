class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Main thing here is find problematic users first then determine which of the language
        """
        # Convert languages to set for faster checks
        user_langs = [set(lang) for lang in languages]

        # Identify problematic friendships and collect problematic users
        problematic_users = set()
        for u, v in friendships:
            u_idx, v_idx = u-1, v-1  # Convert to 0-based indexing

            # Check if users can communicate (have common language)
            if not user_langs[u_idx] & user_langs[v_idx]:
                problematic_users.add(u_idx)
                problematic_users.add(v_idx)

        # No issues, all can communicate
        if not problematic_users:
            return 0

        # Count language usage amongst problematic users
        lang_count = [0] * (n+1)
        for user_idx in problematic_users:
            for lang in user_langs[user_idx]:
                lang_count[lang] += 1

        # Find most popular language amongst problematic users
        max_count = max(lang_count)
        return len(problematic_users) - max_count
