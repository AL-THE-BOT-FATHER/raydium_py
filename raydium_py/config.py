from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore

PRIV_KEY = "base58_string_here"
RPC = "rpc_url_here"
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)