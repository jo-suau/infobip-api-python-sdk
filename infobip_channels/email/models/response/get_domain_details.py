from infobip_channels.core.models import ResponseBase
from infobip_channels.email.models.response.core import ResultDomain


class GetDomainDetailsResponse(ResponseBase, ResultDomain):
    pass
