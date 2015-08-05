# Licensed under a 3-clause BSD style license - see LICENSE.rst
import numpy as np
from astropy import units as u
import os,sys
from .. import spectrum
from .. import utils
epsilon = 1.e-10 #tolerance for floating point errors
sys._called_from_test = True

def generate_spectrum():
  """
  Generate and return a generic spectrum from dummy data
  """
  xdata = np.arange(1000,2000,10)*u.micron
  ydata = np.arange(0,100,1)*utils.unit_od
  return spectrum.BaseSpectrum(xdata,ydata)

def generate_absspectrum():
  """
  Generate and return an absorption spectrum suitable for testing
  """
  filepath_waterice = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/waterice_absorption.txt')
  wn, absorbance = np.loadtxt(filepath_waterice,delimiter=', ',skiprows=0,unpack=True)
  return spectrum.AbsorptionSpectrum(wn*u.kayser,-1.0*np.log(10**(-1.0*absorbance))*utils.unit_od,specname='test water spectrum (absorption)')

def generate_labspectrum():
  """
  Generate and return a lab spectrum (from n and k) suitable for testing
  """
  filepath_waterice = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/waterice_nandk.txt')
  wn, n, k, dum1, dum2 = np.loadtxt(filepath_waterice,skiprows=1,unpack=True)
  return spectrum.LabSpectrum(wn,n,k,specname='test water spectrum (n and k)')
