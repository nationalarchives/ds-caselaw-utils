from typing import NewType

# Types which are used for identifying courts and their jurisdictions
CourtCode = NewType("CourtCode", str)
CourtParam = NewType("CourtParam", str)
JurisdictionCode = NewType("JurisdictionCode", str)

# Types which are used to identify a judgment
NeutralCitationString = NewType("NeutralCitationString", str)
NCNBasedUriString = NewType("NCNBasedUriString", str)
