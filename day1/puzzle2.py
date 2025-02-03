import puzzle1

def get_similarity_score(left, right):
    similarity = 0

    for num in left:
        similarity += num * right.count(num)
    
    return similarity
        

if __name__ == "__main__":
    lists = puzzle1.get_lists()
    print(get_similarity_score(lists[0], lists[1]))