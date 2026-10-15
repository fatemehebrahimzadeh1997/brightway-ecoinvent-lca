# Real-World ecoinvent v3.10 & Brightway2 Matrix Evaluation Pipeline

A production-grade LCA script managing dynamic database querying, structural graph edge discovery, and native matrix calculations utilizing an imported **ecoinvent v3.10 (Cut-Off system model)** library.

This pipeline programmatically filters regional datasets, audits industrial technosphere/biosphere exchanges, searches for verified LCIA climate methodologies, and resolves the global industrial loop paradox using sparse matrix solvers.

## Key Implementation Features
*   **Dynamic regional node filtering:** Uses string comprehensions to filter thousands of background entries, dynamically isolating Swiss-specific (`CH`) production activities.
*   **Graph exchange discovery:** Traverses the process network to audit and isolate every chemical emission and structural input exchange bound to the target activity node.
*   **Metadata-driven method assignment:** Scans the framework's entire methodology tree programmatically to match and bind a validated, available Global Warming Potential (GWP) method.
*   **Native matrix calculation:** Feeds the isolated process demands vector directly into the LCA linear algebra engine, initializing the Technosphere (A) and Biosphere (B) matrices for inversion.

## Core File Inventory
*   `ecoinvent_lca.py`: Clean, simple, functional script tracking genuine database connection routines.
