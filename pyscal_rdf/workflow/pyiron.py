"""
Wrappers for pyiron jobs
"""
import os
from functools import partial, update_wrapper
import pyscal_rdf.workflow.workflow as wf
from pyscal_rdf import KnowledgeGraph, System



def _check_if_job_is_valid(job):
	valid_jobs = ['Lammps', ]
	
	if not type(job).__name__ in valid_jobs:
		raise TypeError('These type of pyiron Job is not currently supported')

