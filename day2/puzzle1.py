def get_reports():
    reports = []
    with open("input.txt", "r") as f:
        for row in f:
            report = list(map(int, row.strip().split(" ")))
            reports.append(report)
    return reports
            

def is_asc_dsc(report: list):
    post_sort_asc = report.copy()
    post_sort_desc = report.copy()
    post_sort_asc.sort()
    post_sort_desc.sort(reverse=True)

    if report == post_sort_asc or report == post_sort_desc:
        return True
    return False


def range_ok(report: list):
    result = True
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i+1])
        if difference not in range(1, 4):
            result = False
    return result


def total_safe_reports(reports):
    total_safe = 0
    for report in reports:
        if range_ok(report) and is_asc_dsc(report):
            total_safe += 1
    
    return total_safe


if __name__ == "__main__":
    print(total_safe_reports(get_reports()))
