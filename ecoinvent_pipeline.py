import bw2data as bd
import bw2calc as bc

bd.projects.set_current("my_real_ecoinvent_project")

DB_NAME = "ecoinvent-3.10-cutoff"

if DB_NAME not in bd.databases:
    raise RuntimeError("Real ecoinvent database not imported.")

db = bd.Database(DB_NAME)

matches = [
    act for act in db
    if "cement" in act["name"].lower()
    and act.get("location") == "CH"
]

for act in matches[:10]:
    print(act["name"], act.get("reference product"))

if not matches:
    raise RuntimeError("No matching Swiss cement activities.")

cement = matches[0]

print("\nSelected activity:", cement["name"])

for exc in cement.exchanges():
    print(
        exc["type"],
        exc.input["name"],
        exc["amount"]
    )

print("\nAvailable climate methods:")
methods = [
    m for m in bd.methods
    if "climate change" in " ".join(m).lower()
    or "global warming" in " ".join(m).lower()
]

for method in methods[:10]:
    print(method)

if not methods:
    raise RuntimeError("No climate LCIA method imported.")

# Select the method only after checking its identity
# and compatibility with the imported inventory.
method = methods[0]

lca = bc.LCA({cement: 1}, method)
lca.lci()
lca.lcia()

print("Climate impact:", lca.score, "kg CO2-eq/kg cement")