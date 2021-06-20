def license_key_formatting(s: str, k: int) -> str:
    no_dashes_str_rev = s.upper().replace("-", "")[::-1]
    new_groups = []
    for i in range(0, len(no_dashes_str_rev), k):
        new_groups.append(no_dashes_str_rev[i: i + k])
    new_groups = new_groups[::-1]
    new_groups = [s[::-1] for s in new_groups]
    return "-".join(new_groups)
