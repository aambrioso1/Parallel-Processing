# Batch run to collect data on MPI program

mpiexec -n 1 python mpi_pi.py
mpiexec -n 2 python mpi_pi.py
mpiexec -n 4 python mpi_pi.py
mpiexec -n 8 python mpi_pi.py
mpiexec -n 16 python mpi_pi.py
mpiexec -n 32 python mpi_pi.py
mpiexec -n 64 python mpi_pi.py
mpiexec -n 128 python mpi_pi.py
