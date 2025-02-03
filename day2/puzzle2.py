import puzzle1

def safe_with_problem_damper(report: list):
    for i in range(len(report)):
        lesser_list = report.copy()
        lesser_list.pop(i)
        if puzzle1.range_ok(lesser_list) and puzzle1.is_asc_dsc(lesser_list):
            return True
    return False


def total_safe_reports(reports):
    total_safe = 0
    for report in reports:
        if safe_with_problem_damper(report):
            total_safe += 1
    
    return total_safe


if __name__ == "__main__":
    print(total_safe_reports(puzzle1.get_reports()))