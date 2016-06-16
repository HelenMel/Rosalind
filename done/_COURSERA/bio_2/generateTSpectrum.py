import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import nucleotides as info

def linearSpectrum(Peptide, AminoAcidMass):
	PrefixMass = [ 0 ]
	for i in xrange(1, len(Peptide) + 1):
		peptideMass = AminoAcidMass[Peptide[i - 1]]
		PrefixMass.append(PrefixMass[i - 1] + peptideMass)
	LinearSpectrum = [0]
	for start in xrange(0, len(Peptide)):
		for end in xrange(start + 1, len(Peptide) + 1):
			LinearSpectrum.append(PrefixMass[end] - PrefixMass[start])
	LinearSpectrum.sort()
	return LinearSpectrum

def linearSpectrumForMassOnly(Peptide):
	PrefixMass = [ 0 ]
	for i in xrange(1, len(Peptide) + 1):
		peptideMass = Peptide[i - 1]
		PrefixMass.append(PrefixMass[i - 1] + peptideMass)
	LinearSpectrum = [0]
	for start in xrange(0, len(Peptide)):
		for end in xrange(start + 1, len(Peptide) + 1):
			LinearSpectrum.append(PrefixMass[end] - PrefixMass[start])
	LinearSpectrum.sort()
	return LinearSpectrum

def cyclicSpectrum(Peptide, AminoAcidMass):
	PrefixMass = [ 0 ]
	for i in xrange(1, len(Peptide) + 1):
		peptideMass = AminoAcidMass[Peptide[i - 1]]
		PrefixMass.append(PrefixMass[i - 1] + peptideMass)
	peptideMass = PrefixMass[-1]
	CyclicSpectrum = [0]
	for start in xrange(0, len(Peptide)):
		for end in xrange(start + 1, len(Peptide) + 1):
			subMass = PrefixMass[end] - PrefixMass[start]
			CyclicSpectrum.append(subMass)
			if start > 0 and end < len(Peptide):
				CyclicSpectrum.append(peptideMass - subMass)
	CyclicSpectrum.sort()
	return CyclicSpectrum

def cyclicSpectrumForMassOnly(Peptide):
	PrefixMass = [ 0 ]
	for i in xrange(1, len(Peptide) + 1):
		peptideMass = Peptide[i - 1]
		PrefixMass.append(PrefixMass[i - 1] + peptideMass)
	peptideMass = PrefixMass[-1]
	CyclicSpectrum = [0]
	for start in xrange(0, len(Peptide)):
		for end in xrange(start + 1, len(Peptide) + 1):
			subMass = PrefixMass[end] - PrefixMass[start]
			CyclicSpectrum.append(subMass)
			if start > 0 and end < len(Peptide):
				CyclicSpectrum.append(peptideMass - subMass)
	CyclicSpectrum.sort()
	return CyclicSpectrum

def generateSpectrum(Peptide):
	return cyclicSpectrum(Peptide,info.massIntTable())

#print generateSpectrum("TLAM")
#print linearSpectrum("MPYENCCCWMFNIRKGQPDFFRKGAVPYVVPMNCIRWS", info.massIntTable())
