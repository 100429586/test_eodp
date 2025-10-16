
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\mesqu\OneDrive\Documentos\GitHub\test_eodp\auxiliary'
indir = r"C:\\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-E2E\myismoutputs"
outdir = r"C:\\Users\mesqu\OneDrive\Escritorio\EODP_TER_2021\EODP-TS-E2E\myl1boutputs_noeq"

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
