
import requests


def dualgraphs20(state, filepath, geometry="block group"):
    """
    Retrieves Lab-processed dual graph data for the provided state and geometry
    level and writes it to the provided filepath.

    Args:
        state (us.State): State for which we retrieve data.
    """
    acceptable = set("bg", "block group", "blockgroup", "vtd")

    if geometry.lower() not in acceptable:
        print(f'Requested geometry "{geometry}" is not allowed; ' "loading block groups.")
        geometry = "bg"

    # Specify the base url.
    base = "http://data.mggg.org.s3-website.us-east-2.amazonaws.com/dual-graphs/"
    suffix = (
        f"{state.abbr.lower()}-{geometry}-connected.json"
    )

    # Send the request!
    request = requests.get(base + suffix)

    with open(filepath, "wb") as w:
        w.write(request.content)


def vtds20(state, filepath):
    """
    Retrieves Lab-processed geometric data for the provided state and geometry
    level and writes it to the provided filepath.

    Args:
        state (us.State): State for which we retrieve data.
    """
    # Specify the base url.
    base = "http://data.mggg.org.s3-website.us-east-2.amazonaws.com/vtd-shapefiles/"
    suffix = (
        f"{state.abbr.upper()}_" f"vtd20.zip"
    )

    # Send the request!
    request = requests.get(base + suffix)

    with open(filepath, "wb") as w:
        w.write(request.content)


def geometries20(state, filepath, geometry="tract"):
    """
    Retrieves Lab-processed geometric data for the provided state and geometry
    level and writes it to the provided filepath.

    Args:
        state (us.State): State for which we retrieve data.
        filepath (str): Location to which we write the compressed data.
        geometry (str, optional): Geometry level at which we retrieve data.
            Accepted values are `block group`, `block`, `congress`, `county`,
            `cousub`, `place`, `senate`, `house`, `tract`, and `vtd`. Defaults
            to `tract`.
    """
    # Create a mapping from standard geometry names to data.mggg.org geometry
    # identifiers.
    geometrymap = {
        "block group": "bg",
        "block": "block",
        "congress": "cd116",
        "county": "county",
        "cousub": "cousub",
        "place": "place",
        "senate": "sldu",
        "house": "sldl",
        "tract": "tract",
        "vtd": "vtd",
    }

    # Check that the passed geometry is allowable.
    if geometry not in set(geometrymap.keys()):
        print(f'Requested geometry "{geometry}" is not allowed; ' "loading tracts.")
        geometry = "tract"

    # Specify the base url.
    base = "http://data.mggg.org.s3-website.us-east-2.amazonaws.com/census-2020/"
    suffix = (
        f"{state.abbr.lower()}/{state.abbr.lower()}_" f"{geometrymap[geometry]}.zip"
    )

    # Send the request!
    request = requests.get(base + suffix)

    with open(filepath, "wb") as w:
        w.write(request.content)
