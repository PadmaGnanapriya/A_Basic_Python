def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    return vote_counts


votes = [1, 2, 1, 3, 1, 3, 3, 2, 2, 4, 5, 5, 4, 2, 4, 2, 1, 2]
vote_counts = majority_vote(votes)
print(vote_counts)
