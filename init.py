def Align(data):
    '''Description
    '''
    training_data = open(data, 'r')
    aligned_sequences = []

    curr_seq = None
    curr_line = training_data.readline()

    while curr_line != '': # populate aligned_sequences from training_data
        if curr_line[0] != '>':
            curr_seq += curr_line[:-1] # remove newline character
        elif curr_line[0] == '>' and curr_seq != None:
            aligned_sequences.append(curr_seq)
            curr_seq = ''
        else:
            curr_seq = ''
        curr_line = training_data.readline()

    training_data.close()

    return aligned_sequences

aligned_sequences = Align('training_data.txt') # test

def Score(aligned_sequences):
    '''Description
    '''
    emission_scores = {} # index -> {curr_letter -> score}
    transition_scores = {} # curr_letter -> {next_letter -> score}

    for seq in range(len(aligned_sequences)): # sequence
        for pos in range(len(aligned_sequences[0])-1): # position
            curr_letter = aligned_sequences[seq][pos]
            next_letter = aligned_sequences[seq][pos+1]

            if emission_scores.has_key(pos): # emission counts
                if emission_scores[pos].has_key(curr_letter):
                    emission_scores[pos][curr_letter] += 1
                else:
                    emission_scores[pos][curr_letter] = 1
            else:
                emission_scores[pos] = {curr_letter: 1}

            if transition_scores.has_key(curr_letter): # transition counts
                if transition_scores[curr_letter].has_key(next_letter):
                    transition_scores[curr_letter][next_letter] += float(1)
                else:
                    transition_scores[curr_letter][next_letter] = float(1)
            else:
                transition_scores[curr_letter] = {next_letter: float(1)}

    for pos in emission_scores: # normalize emissions: counts -> probabilities
        total_count = float(0)
        for curr_letter in emission_scores[pos]:
            total_count += emission_scores[pos][curr_letter]
        for curr_letter in emission_scores[pos]:
            emission_scores[pos][curr_letter] /= total_count

    for curr_letter in transition_scores: # normalize transitions: counts -> probabilities
        total_count = float(0)
        for next_letter in transition_scores[curr_letter]:
            total_count += transition_scores[curr_letter][next_letter]
        for next_letter in transition_scores[curr_letter]:
            transition_scores[curr_letter][next_letter] /= total_count

    # display output

    for curr_index in emission_scores:
        print 'curr_index:', curr_index
        print emission_scores[curr_index], '\n'

    for curr_letter in transition_scores:
        print "curr_letter:", curr_letter
        print transition_scores[curr_letter], '\n'

    return (emission_scores, transition_scores)

scores = Score(aligned_sequences) # test
