# server.py

from fastmcp import FastMCP
from rdkit import Chem

mcp = FastMCP("My rdkit server")

@mcp.tool()
def mutate_smiles(smi):
    """input smiles를 같은 분자를 지칭하지만 다른 smiles 표현법으로 변환합니다"""
    mol = Chem.MolFromSmiles(smi)
    mutated_smiles = Chem.MolToSmiles(mol, doRandom=True)

    return mutated_smiles

if __name__ == "__main__":
    mcp.run()