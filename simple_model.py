from pysb import *


Model()

# Declare the cells as Monomers
Monomer('Hepatoblast')
Monomer('Hepatocyte')
Monomer('Cholangiocyte')

# Declare the parameters
Parameter('Hepatoblast_0', 200)
Parameter('Hepatocyte_0', 0)
Parameter('Cholangiocyte_0', 0)

Parameter('hepatoblast_division_rate', 1/24)
Parameter('hepatocyte_division_rate', 1/24)
Parameter('cholangiocyte_division_rate', 1/24)

Parameter('hepatoblast_bipotent_division_rate', 1/24)
Parameter('hepatoblast_unipotent_hepatocyte_division_rate', 1/24)
Parameter('hepatoblast_unipotent_cholangiocyte_division_rate', 1/24)

# Declare the initial conditions
Initial(Hepatoblast(), Hepatoblast_0)
Initial(Hepatocyte(), Hepatocyte_0)
Initial(Cholangiocyte(), Cholangiocyte_0)

# Declare the cell division rule
Rule('Hepatoblast_symmetric_division', Hepatoblast() >> Hepatoblast() + Hepatoblast(), hepatoblast_division_rate)
Rule('Hepatocyte_division', Hepatocyte() >> Hepatocyte() + Hepatocyte(), hepatocyte_division_rate)
Rule('Cholangiocyte_division', Cholangiocyte() >> Cholangiocyte() + Cholangiocyte(), cholangiocyte_division_rate)

Rule('Hepatoblast_bipotent_division', Hepatoblast() >> Hepatocyte() + Cholangiocyte(), hepatoblast_bipotent_division_rate)
Rule('Hepatoblast_unipotent_hepatocyte_division', Hepatoblast() >> Hepatocyte() + Hepatocyte(), hepatoblast_unipotent_hepatocyte_division_rate)
Rule('Hepatoblast_unipotent_cholangiocyte_division', Hepatoblast() >> Cholangiocyte() + Cholangiocyte(), hepatoblast_unipotent_cholangiocyte_division_rate)

# Observe the cells
Observable('Hepatoblasts', Hepatoblast())
Observable('Hepatocytes', Hepatocyte())
Observable('Cholangiocytes', Cholangiocyte())