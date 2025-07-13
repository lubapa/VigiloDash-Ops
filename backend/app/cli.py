# import typer
# from app.services.proxmox import get_vms

# cli = typer.Typer()

# @cli.command()
# def vms(state: str = typer.Option(None, help="on | off")):
#     vms = get_vms(state)
#     for vm in vms:
#         print(f"{vm['vmid']} - {vm['name']} - {vm['status']}")

# if __name__ == "__main__":
#     cli()
