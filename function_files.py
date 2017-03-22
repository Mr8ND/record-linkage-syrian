align_symbol = "$"


def countInsertion1gram(align_pair):
    return (sum ([x==str(align_symbol) for x in align_pair[0]]))

def countDeletion1gram(align_pair):
    return (sum([x==str(align_symbol) for x in align_pair[1]]))

def countIdentity1gram(align_pair):
    return (sum([x==y for x,y in zip(align_pair[0], align_pair[1])]))


feature_dict={
    '1gram_deletion': countDeletion1gram,
    '1gram_insertion': countInsertion1gram,
    '1gram_identity': countIdentity1gram
}