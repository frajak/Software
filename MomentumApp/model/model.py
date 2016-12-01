from epics import caget,caput
import os,sys
import time
import generalMomentumFunctions as general
sys.path.append('C:\\Users\\wln24624\\Documents\\VELA-CLARA-Controllers\\Controllers\\VELA\INJECTOR\\velaINJMagnets\\bin\\Release')
import logging
#import velaINJMagnetControl as vimc


class Model():
	def __init__(self, view):
		#Loggers
		self.PL = logging.getLogger("P")
		self.PSL = logging.getLogger("PS")
		self.deets = logging.getLogger("P/PS")

		#Important values to notes
		self.p = 0
		self.I = 0
		self.ps = 0
		self.Is = 0
		self.predictedMomentum = 0
		self.predictedI = 0

		#Generic momentum procedures
		self.func = general.Functions()

		#Magnet, BPM and screen controllers
		#self.magnets =	vimc.velaINJMagnetController(False,False,False)
		self.view = view
		print("Model Initialized")


	#Outline of Momentum Measurement Procedure
	def measureMomentum(self):

		#1. Preliminaries
		if self.view.checkBox_1.isChecked()==True:
			self.PL.info('1. Preliminaries')

		#2. Align Beam through Dipole
		if self.view.checkBox_2.isChecked()==True:
			self.PL.info('2. Aligning Beam through Dipole')
			for i in range(3):
				self.func.align('HCOR01','BPM01', self.deets)
				self.func.align('HCOR02','BPM02', self.deets)

		#3. Centre in Spec. Line
		if self.view.checkBox_3.isChecked()==True:
			self.PL.info('3. Center Down Spec. Line')
			self.func.bendBeam('DIP01','BPM03', self.predictedI, self.deets)

		#4. Convert Current to Momentum
		if self.view.checkBox_4.isChecked()==True:
			self.PL.info('4. Calculate Momentum')
			self.func.calcMom(self.deets)


	#Outline of Momentum Spread Measurement Procedure
	def measureMomentumSpread(self):
		if self.view.checkBox_done_mom.isChecked()==True:
			"""2. Set Disperaion"""
			if self.view.checkBox_1_s.isChecked()==True:
				"""1. Checks"""
				self.PSL.info('1. Run Checks')
				self.func.minimizeBeta('QUAD01','YAG05',self.deets)

			"""2. Set Disperaion"""
			if self.view.checkBox_2_s.isChecked()==True:
				"""2.1 Minimize Beta"""
				self.PSL.info('2.1 Minimize Beta')
				self.func.minimizeBeta('QUAD01','YAG05',self.deets)

				"""2.2 Set Dispersion Size on Spec Line"""
				self.PSL.info('2.2 Minimize Beta')
				self.func.fixDispersion('QUAD06','YAG04',self.deets)

			"""3. Calculate Dispersion """
			if self.view.checkBox_3_s.isChecked()==True:
				self.PSL.info('3. Dertermine Dispersion')
				self.func.findDispersion('DIP01','YAG04',self.deets)

			"""4. Calculate Momenum Spread """
			if self.view.checkBox_4_s.isChecked()==True:
				self.PSL.info('4. Get Momentum Spread')
				self.func.calcMomSpread(self.deets)
		else:
			self.PSL.error('Not confirmed momentum measurement')

		def setPredictedMom(self):
			self.predictedMomentum = self.view.lineEdit_predictMom.text()
			self.func.predictedMomentum = self.view.lineEdit_predictMom.text()
