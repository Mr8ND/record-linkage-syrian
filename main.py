from function_files import align_symbol, feature_dict
from utilities import ngramFunction


def featureExtraction(align_pair, feature_list):
    output_vec = []
    for i,feat in enumerate(feature_list):
        output_vec.append(feature_dict[feat](align_pair))
    return output_vec

def main(align_pair):
	print featureExtraction(align_pair, feature_dict.keys())


if __name__ == '__main__':
	ex_pair = ('robert', 'rob'+align_symbol+'rt')
	N = 2
	main(ex_pair)
	print zip(ngramFunction(ex_pair[0], N),ngramFunction(ex_pair[1], N))
