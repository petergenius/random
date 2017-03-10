#!/usr/bin/env python3
class WriteError(Exception):
    pass
class ReadError(Exception):
    pass
def write_score(score, name, scores, filename, sep=','):
    """writes a score with a name to a file, in a specified format"""
    if score == '' or name == '' or sep in name:
        raise WriteError('Either the score({}) or name({}) was blank, or the file seperator ({}) was in the name.'.format(score, name, sep))
    score_tuple = (score,name)
    scores.append(score_tuple)
    with open(filename,'w') as f:
        for s in scores:
            f.write(sep.join(map(str, s)) + '\n')

def read_scores(filename, sep=','):
    """reads scores and names from a file, and returns a list of each"""
    
    scores = []
    names = []
    
    with open(filename) as f:
        for score_line in f:
            score, name = score_line.strip().split(sep)
            scores.append(int(score))
            names.append(name)

    return scores, names

def sort_scores(scores, names,reverse_bool=True):
    """sorts the scores from greatest to least and returns in a list of tuples format"""
    return sorted(zip(scores,names), reverse=reverse_bool)

def print_scores(score_list, sep=' ', top_amount=5):
    """prints the number of leaderboard scores stated"""
    for score_tuple in score_list[:top_amount]:
        print(sep.join(map(str, score_tuple)))

def has_better_score(score, scores, leaderboard_len=5):
    """returns if the score should be written to a file"""
    return (len(scores) > leaderboard_len and score >= scores[leaderboard_len - 1][0]) or len(scores) <= leaderboard_len
