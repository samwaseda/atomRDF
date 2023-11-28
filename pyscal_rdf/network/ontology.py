from pyscal_rdf.network.network import OntologyNetwork
import os

#prov = OntologyNetwork('pyscal_rdf/data/prov.rdf', delimiter='#')
def read_ontology():
	#read in ontologies
	cmso = OntologyNetwork('../pyscal_rdf/data/cmso.owl')
	pldo = OntologyNetwork('../pyscal_rdf/data/pldo.owl')
	podo = OntologyNetwork('../pyscal_rdf/data/podo.owl')
	#msmo = OntologyNetwork('../pyscal_rdf/data/msmo.owl')
	
	#combine them
	combo = cmso + pldo + podo + msmo	
	
	#add namespaces
	#combo.add_namespace('prov', 'http://www.w3.org/ns/prov#')
	combo.add_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
	combo.add_namespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
	
	#add extra terms for quering
	#combo.add_term('http://www.w3.org/ns/prov#Entity', 'class', delimiter='#')
	#combo.add_term('http://www.w3.org/ns/prov#Activity', 'class', delimiter='#')
	#combo.add_term('http://www.w3.org/ns/prov#SoftwareAgent', 'class', delimiter='#')
	#combo.add_term('http://www.w3.org/ns/prov#wasDerivedFrom', 'object_property', delimiter='#')
	#combo.add_term('http://www.w3.org/ns/prov#wasGeneratedBy', 'object_property', delimiter='#')
	#combo.add_term('http://www.w3.org/ns/prov#wasAssociatedWith', 'object_property', delimiter='#')
	#combo.add_term('http://www.w3.org/ns/prov#actedOnBehalfOf', 'object_property', delimiter='#')
	combo.add_term('http://www.w3.org/2000/01/rdf-schema#label', 'data_property', delimiter='#', namespace='rdfs')
	combo.add_term('http://www.w3.org/1999/02/22-rdf-syntax-ns#type', 'object_property', delimiter='#', namespace='rdf')
	
	#add paths
	combo.add_path(('cmso:Material', 'cmso:hasDefect', 'pldo:PlanarDefect'))
	combo.add_path(('cmso:Material', 'cmso:hasDefect', 'podo:Vacancy'))
	combo.add_path(('cmso:SimulationCell', 'podo:hasVacancyConcentration', 'float'))
	combo.add_path(('cmso:SimulationCell', 'podo:hasNumberOfVacancies', 'int'))
	#combo.add_path(('cmso:ComputationalSample', 'prov:wasDerivedFrom', 'cmso:ComputationalSample'))
	#combo.add_path(('cmso:ComputationalSample', 'prov:wasGeneratedBy', 'msmo:ComputationalMethod'))
	#combo.add_path(('msmo:ComputationalMethod', 'prov:wasAssociatedWith', 'prov:SoftwareAgent'))
	combo.add_path(('cmso:ComputationalSample', 'rdf:type', 'prov:Entity'))
	#combo.add_path(('msmo:ComputationalMethod', 'rdf:type', 'prov:Activity'))
	#for Alt Name, maybe this should not be here
	combo.add_path(('cmso:CrystalStructure', 'cmso:hasAltName', 'string'))
	
	#return
	return combo