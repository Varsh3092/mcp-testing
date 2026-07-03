from mcp.server.fastmcp import FastMCP

from tools.register_tool import (
    get_register_details
)

mcp = FastMCP(
    "Embedded Register MCP"
)


@mcp.tool()
def explain_register(
    pdf_path: str,
    register_name: str
):
    """
    Get detailed register information
    from a datasheet or register
    specification PDF.
    """

    return get_register_details(
        pdf_path,
        register_name
    )


#if __name__ == "__main__":
    #mcp.run()
    
if __name__ == "__main__":

    result = explain_register(
        pdf_path=r"C:\Users\varsha.somasundaram\Downloads\PCIE-sprugs6d.pdf",
        register_name="PCIE_SERDES_CFGPLL"
    )

    print(result)
