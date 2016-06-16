import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import nucleotides as info
import generateTSpectrum as gTS

def score(Peptide, Spectrum, AminoAcidMass):
	theorySpectrum = gTS.cyclicSpectrum(Peptide, AminoAcidMass)
	return scoreBetweenSpectrums(theorySpectrum, Spectrum)

def scoreM(Peptide, Spectrum):
	theorySpectrum = gTS.cyclicSpectrumForMassOnly(Peptide)
	return scoreBetweenSpectrums(theorySpectrum, Spectrum)

def linearScore(Peptide, Spectrum, AminoAcidMass):
	theorySpectrum = gTS.linearSpectrum(Peptide, AminoAcidMass)
	return scoreBetweenSpectrums(theorySpectrum, Spectrum)

def linearScoreM(Peptide, Spectrum):
	theorySpectrum = gTS.linearSpectrumForMassOnly(Peptide)
	return scoreBetweenSpectrums(theorySpectrum, Spectrum)

def scoreBetweenSpectrums(GeneratedSpectrum, Spectrum):
	score = 0
	for mass in Spectrum:
		try:
			GeneratedSpectrum.remove(mass)
		except ValueError:
			continue
		score += 1
	return score

#print linearScore("NQEL", [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484], info.massIntTable())
