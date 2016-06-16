import copy
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import nucleotides as info
import generateTSpectrum as gTS

def cyclopeptideSequencing(Spectrum):
	Sequencings = []
	massSet = info.massIntSet()
	Peptides = []
	Peptides.append([])
	ParentMass = Spectrum[-1]
	while len(Peptides) > 0:
		Peptides = expand(Peptides, massSet)
		Peptides_ = []
		for Peptide in Peptides:
			if sum(Peptide) >= ParentMass:
				if gTS.cyclicSpectrumForMassOnly(Peptide) == Spectrum:
					Sequencings.append(Peptide)
			else:
				if isConsitent(Peptide, Spectrum) is True:
					Peptides_.append(Peptide)
		Peptides = Peptides_
	return Sequencings

def expand(Peptides, MassSet):
	newPeptides = []
	for Peptide in Peptides:
		def peptideExtension(mass, origPeptide):
			newP = copy.copy(origPeptide)
			newP.append(mass)
			return newP
		newPeptides += [peptideExtension(mass, Peptide) for mass in MassSet]
	return newPeptides

def isConsitent(Peptide, Spectrum):
	spectrumCopy = copy.copy(Spectrum)
	SpectrumP = gTS.linearSpectrumForMassOnly(Peptide)
	for mass in SpectrumP:
		try:
			spectrumCopy.remove(mass)
		except ValueError:
			return False
	return True

def isConsitent(Peptide, Spectrum, AminoAcidMass):
	spectrumCopy = copy.copy(Spectrum) 
	SpectrumP = gTS.linearSpectrum(Peptide, AminoAcidMass)
	for mass in SpectrumP:
		try:
			spectrumCopy.remove(mass)
		except ValueError:
			return False
	return True

#print isConsitent("ETC",[0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333], info.massIntTable())

