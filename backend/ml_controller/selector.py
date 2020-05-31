from typing import List


def getLinks(int: n) -> List[str]:
    if n == 0:
        return ["https://www.canadahelps.org/en/donate-to-coronavirus-outbreak-response/",
                "https://www.gofundme.com/c/blog/fundraising-for-coronavirus",
                "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donate"]

    elif n == 1:
        return ["https://www.globalgiving.org/climate-action-fund/",
                "https://www.idinsight.org/givinggreen",
                "https://www.canadahelps.org/en/explore/charities/category/environment/"]

    elif n == 2:
        return ["https://ca.gofundme.com/f/georgefloyd",
                "https://www.change.org/p/mayor-jacob-frey-justice-for-george-floyd",
                "https://www.blackvisionsmn.org/"]

    return [""]
