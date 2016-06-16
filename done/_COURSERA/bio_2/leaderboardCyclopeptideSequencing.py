import copy
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import nucleotides as info
import generateTSpectrum as gTS
import cyclopeptideScoring as cS
import cyclopeptideSequencing as cSing

def leaderboardCyclopeptideSequencing(Spectrum, N):
	return leaderboardCyclopeptideSequencingWithMass(Spectrum, N, info.massIntSet())

def leaderboardCyclopeptideSequencingWithMass(Spectrum, N, massSet):
	LeaderPeptide = ("", 0)
	Leaderboard = []
	Leaderboard.append([])
	ParentMass = Spectrum[-1]
	while len(Leaderboard) > 0:
		Leaderboard = cSing.expand(Leaderboard, massSet)
		Leaderboard_ = copy.copy(Leaderboard)
		for Peptide in Leaderboard:
			PeptideMass = sum(Peptide)
			if PeptideMass == ParentMass:
				score_ = cS.scoreM(Peptide, Spectrum)
				if score_ > LeaderPeptide[1]:
					LeaderPeptide = (Peptide, score_)
			else:
				if PeptideMass > ParentMass:
					Leaderboard_.remove(Peptide)
		Leaderboard = trimM(Leaderboard_, Spectrum, N)
	return LeaderPeptide

def trimM(Leaderboard, Spectrum, N):
	def toLinearScoreItem(p, Spectrum):
		return (p, cS.linearScoreM(p, Spectrum))
	LinearScoreTable = [toLinearScoreItem(p, Spectrum) for p in Leaderboard]
	LinearScoreTable = sorted(LinearScoreTable, key= lambda tup: tup[1], reverse = True)
	for j in xrange(N, len(Leaderboard)):
		if LinearScoreTable[j][1] < LinearScoreTable[N - 1][1]:
			LinearScoreTable = LinearScoreTable[:j]
			break
	return [x[0] for x in LinearScoreTable]

def trim(Leaderboard, Spectrum, N, MassTable):
	def toLinearScoreItem(p, Spectrum, MassTable):
		return (p, cS.linearScore(p, Spectrum, MassTable))
	LinearScoreTable = [toLinearScoreItem(p, Spectrum, MassTable) for p in Leaderboard]
	LinearScoreTable = sorted(LinearScoreTable, key= lambda tup: tup[1], reverse = True)
	for j in xrange(N, len(Leaderboard)):
		if LinearScoreTable[j][1] < LinearScoreTable[N - 1][1]:
			LinearScoreTable = LinearScoreTable[:j]
			break
	return [x[0] for x in LinearScoreTable]

#board = ["LAST", "ALST", "TLLT", "TQAS"]
#Spec = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
#print trim(board, Spec, 2, info.massIntTable())