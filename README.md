Sybilguard algorithm to detect fake accounts in a social network
=======================================================

Social graphs and Random Walks. Implemented in Python



This project aims at proposing a method based on random walks, to automatically detect fake accounts that people might create in a social network. It is based on the algorithm SybilGuard, a novative method created to crack down on fake accounts creation. In this project, we try to use this algorithm to define a detection criterion for the fake accounts of the Caltech network.
This project has been done in the Programming Course at ENSAE ParisTech in 2012, in collaboration with Morgane AUSTERN.

- The first part of this project aims at explaining the mathematical concepts used in the algorithm: random walks, social graphs theory... 

- The second part of this project is a description of the implementation of the algorithm and the construction of a 'detection criterion' using a random adjacency matrix computed so that it has the same characteristics of our real network (Caltech36).

The final part of this project analyzes the results of the algorithm, and the issues met during its developpment.


========================================================

Data used: Caltech36


=======================================================

Files:

- AUSTERN_LAUGEL.pdf : PDF report of the project (in English)
- fake_accounts_detection.py : Python script of the whole project
- test_matrix.py : Python script for the generation of a random social matrix based on the Caltech matrix
- Sybilguard.pdf : Article presenting the algorithm SybilGuard
- Caltech36 : Caltech data
