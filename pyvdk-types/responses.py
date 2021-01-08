from typing import Optional, Union, Any, List, Tuple
import enum

from pydantic import BaseModel as PydanticModel


from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
from . import objects
class AccountChangepasswordResponse(PydanticModel):
    response: Optional[object] = None


class AccountGetactiveoffersResponse(PydanticModel):
    response: Optional[object] = None


class AccountGetapppermissionsResponse(PydanticModel):
    response: Optional[int] = None


class AccountGetbannedResponse(PydanticModel):
    response: Optional[object] = None


class AccountGetcountersResponse(PydanticModel):
    response: Optional["objects.AccountAccountCounters"] = None


class AccountGetinfoResponse(PydanticModel):
    response: Optional["objects.AccountInfo"] = None


class AccountGetprofileinfoResponse(PydanticModel):
    response: Optional["objects.AccountUserSettings"] = None


class AccountGetpushsettingsResponse(PydanticModel):
    response: Optional["objects.AccountPushSettings"] = None


class AccountSaveprofileinfoResponse(PydanticModel):
    response: Optional[object] = None


class AdsAddofficeusersResponse(PydanticModel):
    response: Optional[bool] = None


class AdsChecklinkResponse(PydanticModel):
    response: Optional["objects.AdsLinkStatus"] = None


class AdsCreateadsResponse(PydanticModel):
    response: Optional[List[int]] = None


class AdsCreatecampaignsResponse(PydanticModel):
    response: Optional[List[int]] = None


class AdsCreateclientsResponse(PydanticModel):
    response: Optional[List[int]] = None


class AdsCreatetargetgroupResponse(PydanticModel):
    response: Optional[object] = None


class AdsDeleteadsResponse(PydanticModel):
    response: Optional[List[int]] = None


class AdsDeletecampaignsResponse(PydanticModel):
    response: Optional[int] = None


class AdsDeleteclientsResponse(PydanticModel):
    response: Optional[int] = None


class AdsGetaccountsResponse(PydanticModel):
    response: Optional[List["objects.AdsAccount"]] = None


class AdsGetadslayoutResponse(PydanticModel):
    response: Optional[List["objects.AdsAdLayout"]] = None


class AdsGetadstargetingResponse(PydanticModel):
    response: Optional[List["objects.AdsTargSettings"]] = None


class AdsGetadsResponse(PydanticModel):
    response: Optional[List["objects.AdsAd"]] = None


class AdsGetbudgetResponse(PydanticModel):
    response: Optional[int] = None


class AdsGetcampaignsResponse(PydanticModel):
    response: Optional[List["objects.AdsCampaign"]] = None


class AdsGetcategoriesResponse(PydanticModel):
    response: Optional[object] = None


class AdsGetclientsResponse(PydanticModel):
    response: Optional[List["objects.AdsClient"]] = None


class AdsGetdemographicsResponse(PydanticModel):
    response: Optional[List["objects.AdsDemoStats"]] = None


class AdsGetfloodstatsResponse(PydanticModel):
    response: Optional["objects.AdsFloodStats"] = None


class AdsGetlookalikerequestsResponse(PydanticModel):
    response: Optional[object] = None


class AdsGetmusiciansResponse(PydanticModel):
    response: Optional[object] = None


class AdsGetofficeusersResponse(PydanticModel):
    response: Optional[List["objects.AdsUsers"]] = None


class AdsGetpostsreachResponse(PydanticModel):
    response: Optional[List["objects.AdsPromotedPostReach"]] = None


class AdsGetrejectionreasonResponse(PydanticModel):
    response: Optional["objects.AdsRejectReason"] = None


class AdsGetstatisticsResponse(PydanticModel):
    response: Optional[List["objects.AdsStats"]] = None


class AdsGetsuggestionsCitiesResponse(PydanticModel):
    response: Optional[List["objects.AdsTargSuggestionsCities"]] = None


class AdsGetsuggestionsRegionsResponse(PydanticModel):
    response: Optional[List["objects.AdsTargSuggestionsRegions"]] = None


class AdsGetsuggestionsResponse(PydanticModel):
    response: Optional[List["objects.AdsTargSuggestions"]] = None


class AdsGetsuggestionsSchoolsResponse(PydanticModel):
    response: Optional[List["objects.AdsTargSuggestionsSchools"]] = None


class AdsGettargetgroupsResponse(PydanticModel):
    response: Optional[List["objects.AdsTargetGroup"]] = None


class AdsGettargetingstatsResponse(PydanticModel):
    response: Optional["objects.AdsTargStats"] = None


class AdsGetuploadurlResponse(PydanticModel):
    response: Optional[str] = None


class AdsGetvideouploadurlResponse(PydanticModel):
    response: Optional[str] = None


class AdsImporttargetcontactsResponse(PydanticModel):
    response: Optional[int] = None


class AdsRemoveofficeusersResponse(PydanticModel):
    response: Optional[bool] = None


class AdsUpdateadsResponse(PydanticModel):
    response: Optional[List[int]] = None


class AdsUpdatecampaignsResponse(PydanticModel):
    response: Optional[int] = None


class AdsUpdateclientsResponse(PydanticModel):
    response: Optional[int] = None


class AdsUpdateofficeusersResponse(PydanticModel):
    response: Optional[List["objects.AdsUpdateofficeusersResult"]] = None


class AdswebGetadcategoriesResponse(PydanticModel):
    response: Optional[object] = None


class AdswebGetadunitcodeResponse(PydanticModel):
    response: Optional[object] = None


class AdswebGetadunitsResponse(PydanticModel):
    response: Optional[object] = None


class AdswebGetfraudhistoryResponse(PydanticModel):
    response: Optional[object] = None


class AdswebGetsitesResponse(PydanticModel):
    response: Optional[object] = None


class AdswebGetstatisticsResponse(PydanticModel):
    response: Optional[object] = None


class AppwidgetsGetappimageuploadserverResponse(PydanticModel):
    response: Optional[object] = None


class AppwidgetsGetappimagesResponse(PydanticModel):
    response: Optional["objects.AppwidgetsPhotos"] = None


class AppwidgetsGetgroupimageuploadserverResponse(PydanticModel):
    response: Optional[object] = None


class AppwidgetsGetgroupimagesResponse(PydanticModel):
    response: Optional["objects.AppwidgetsPhotos"] = None


class AppwidgetsGetimagesbyidResponse(PydanticModel):
    response: Optional[List["objects.AppwidgetsPhoto"]] = None


class AppwidgetsSaveappimageResponse(PydanticModel):
    response: Optional["objects.AppwidgetsPhoto"] = None


class AppwidgetsSavegroupimageResponse(PydanticModel):
    response: Optional["objects.AppwidgetsPhoto"] = None


class AppsGetcatalogResponse(PydanticModel):
    response: Optional[object] = None


class AppsGetfriendslistResponse(PydanticModel):
    response: Optional[object] = None


class AppsGetleaderboardExtendedResponse(PydanticModel):
    response: Optional[object] = None


class AppsGetleaderboardResponse(PydanticModel):
    response: Optional[object] = None


class AppsGetscopesResponse(PydanticModel):
    response: Optional[object] = None


class AppsGetscoreResponse(PydanticModel):
    response: Optional[int] = None


class AppsGetResponse(PydanticModel):
    response: Optional[object] = None


class AppsSendrequestResponse(PydanticModel):
    response: Optional[int] = None


class AuthRestoreResponse(PydanticModel):
    response: Optional[object] = None


class BaseBoolResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class BaseGetuploadserverResponse(PydanticModel):
    response: Optional["objects.BaseUploadServer"] = None


class BaseOkResponse(PydanticModel):
    response: Optional[int] = None


class BoardAddtopicResponse(PydanticModel):
    response: Optional[int] = None


class BoardCreatecommentResponse(PydanticModel):
    response: Optional[int] = None


class BoardGetcommentsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class BoardGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class BoardGettopicsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class BoardGettopicsResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetchairsResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetcitiesbyidResponse(PydanticModel):
    response: Optional[List["objects.BaseObject"]] = None


class DatabaseGetcitiesResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetcountriesbyidResponse(PydanticModel):
    response: Optional[List["objects.BaseCountry"]] = None


class DatabaseGetcountriesResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetfacultiesResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetmetrostationsbyidResponse(PydanticModel):
    response: Optional[List["objects.DatabaseStation"]] = None


class DatabaseGetmetrostationsResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetregionsResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetschoolclassesResponse(PydanticModel):
    response: Optional[List[List[Union[str, int]]]] = None


class DatabaseGetschoolsResponse(PydanticModel):
    response: Optional[object] = None


class DatabaseGetuniversitiesResponse(PydanticModel):
    response: Optional[object] = None


class DocsAddResponse(PydanticModel):
    response: Optional[int] = None


class DocsGetbyidResponse(PydanticModel):
    response: Optional[List["objects.DocsDoc"]] = None


class DocsGettypesResponse(PydanticModel):
    response: Optional[object] = None


class DocsGetuploadserver(PydanticModel):
    response: Optional["objects.BaseUploadServer"] = None


class DocsGetResponse(PydanticModel):
    response: Optional[object] = None


class DocsSaveResponse(PydanticModel):
    response: Optional[object] = None


class DocsSearchResponse(PydanticModel):
    response: Optional[object] = None


class DonutGetsubscriptionResponse(PydanticModel):
    response: Optional["objects.DonutDonatorSubscriptionInfo"] = None


class DonutGetsubscriptionsResponse(PydanticModel):
    response: Optional[object] = None


class DownloadedgamesPaidStatusResponse(PydanticModel):
    response: Optional[object] = None


class FaveAddtagResponse(PydanticModel):
    response: Optional["objects.FaveTag"] = None


class FaveGetpagesResponse(PydanticModel):
    response: Optional[object] = None


class FaveGettagsResponse(PydanticModel):
    response: Optional[object] = None


class FaveGetExtendedResponse(PydanticModel):
    response: Optional[object] = None


class FaveGetResponse(PydanticModel):
    response: Optional[object] = None


class FriendsAddlistResponse(PydanticModel):
    response: Optional[object] = None


class FriendsAddResponse(PydanticModel):
    response: Optional[int] = None


class FriendsArefriendsExtendedResponse(PydanticModel):
    response: Optional[List["objects.FriendsFriendExtendedStatus"]] = None


class FriendsArefriendsResponse(PydanticModel):
    response: Optional[List["objects.FriendsFriendStatus"]] = None


class FriendsDeleteResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetappusersResponse(PydanticModel):
    response: Optional[List[int]] = None


class FriendsGetbyphonesResponse(PydanticModel):
    response: Optional[List["objects.FriendsUserXtrPhone"]] = None


class FriendsGetlistsResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetmutualResponse(PydanticModel):
    response: Optional[List[int]] = None


class FriendsGetmutualTargetUidsResponse(PydanticModel):
    response: Optional[List["objects.FriendsMutualFriend"]] = None


class FriendsGetonlineOnlineMobileResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetonlineResponse(PydanticModel):
    response: Optional[List[int]] = None


class FriendsGetrecentResponse(PydanticModel):
    response: Optional[List[int]] = None


class FriendsGetrequestsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetrequestsNeedMutualResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetrequestsResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetsuggestionsResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetFieldsResponse(PydanticModel):
    response: Optional[object] = None


class FriendsGetResponse(PydanticModel):
    response: Optional[object] = None


class FriendsSearchResponse(PydanticModel):
    response: Optional[object] = None


class GiftsGetResponse(PydanticModel):
    response: Optional[object] = None


class GroupsAddaddressResponse(PydanticModel):
    response: Optional["objects.GroupsAddress"] = None


class GroupsAddcallbackserverResponse(PydanticModel):
    response: Optional[object] = None


class GroupsAddlinkResponse(PydanticModel):
    response: Optional["objects.GroupsGroupLink"] = None


class GroupsCreateResponse(PydanticModel):
    response: Optional["objects.GroupsGroup"] = None


class GroupsEditaddressResponse(PydanticModel):
    response: Optional["objects.GroupsAddress"] = None


class GroupsGetaddressesResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetbannedResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetbyidLegacyResponse(PydanticModel):
    response: Optional[List["objects.GroupsGroupFull"]] = None


class GroupsGetbyidResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetcallbackconfirmationcodeResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetcallbackserversResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetcallbacksettingsResponse(PydanticModel):
    response: Optional["objects.GroupsCallbackSettings"] = None


class GroupsGetcataloginfoExtendedResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetcataloginfoResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetcatalogResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetinvitedusersResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetinvitesExtendedResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetinvitesResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetlongpollserverResponse(PydanticModel):
    response: Optional["objects.GroupsLongPollServer"] = None


class GroupsGetlongpollsettingsResponse(PydanticModel):
    response: Optional["objects.GroupsLongPollSettings"] = None


class GroupsGetmembersFieldsResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetmembersFilterResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetmembersResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetrequestsFieldsResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetrequestsResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetsettingsResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGettaglistResponse(PydanticModel):
    response: Optional[List["objects.GroupsGroupTag"]] = None


class GroupsGettokenpermissionsResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetExtendedResponse(PydanticModel):
    response: Optional[object] = None


class GroupsGetResponse(PydanticModel):
    response: Optional[object] = None


class GroupsIsmemberExtendedResponse(PydanticModel):
    response: Optional[object] = None


class GroupsIsmemberResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class GroupsIsmemberUserIdsExtendedResponse(PydanticModel):
    response: Optional[List["objects.GroupsMemberStatusFull"]] = None


class GroupsIsmemberUserIdsResponse(PydanticModel):
    response: Optional[List["objects.GroupsMemberStatus"]] = None


class GroupsSearchResponse(PydanticModel):
    response: Optional[object] = None


class LikesAddResponse(PydanticModel):
    response: Optional[object] = None


class LikesDeleteResponse(PydanticModel):
    response: Optional[object] = None


class LikesGetlistExtendedResponse(PydanticModel):
    response: Optional[object] = None


class LikesGetlistResponse(PydanticModel):
    response: Optional[object] = None


class LikesIslikedResponse(PydanticModel):
    response: Optional[object] = None


class MarketAddalbumResponse(PydanticModel):
    response: Optional[object] = None


class MarketAddResponse(PydanticModel):
    response: Optional[object] = None


class MarketCreatecommentResponse(PydanticModel):
    response: Optional[int] = None


class MarketDeletecommentResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class MarketGetalbumbyidResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetalbumsResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetbyidExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetbyidResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetcategoriesNewResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetcategoriesResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetgroupordersResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetorderbyidResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetorderitemsResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetordersExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetordersResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MarketGetResponse(PydanticModel):
    response: Optional[object] = None


class MarketRestorecommentResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class MarketSearchExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MarketSearchResponse(PydanticModel):
    response: Optional[object] = None


class MessagesCreatechatResponse(PydanticModel):
    response: Optional[int] = None


class MessagesDeletechatphotoResponse(PydanticModel):
    response: Optional[object] = None


class MessagesDeleteconversationResponse(PydanticModel):
    response: Optional[object] = None


class MessagesDeleteResponse(PydanticModel):
    response: Optional[object] = None


class MessagesEditResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class MessagesGetbyconversationmessageidResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetbyidExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetbyidResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetchatpreviewResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetchatChatIdsFieldsResponse(PydanticModel):
    response: Optional[List["objects.MessagesChatFull"]] = None


class MessagesGetchatChatIdsResponse(PydanticModel):
    response: Optional[List["objects.MessagesChat"]] = None


class MessagesGetchatFieldsResponse(PydanticModel):
    response: Optional["objects.MessagesChatFull"] = None


class MessagesGetchatResponse(PydanticModel):
    response: Optional["objects.MessagesChat"] = None


class MessagesGetconversationmembersResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetconversationsbyidExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetconversationsbyidResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetconversationsResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGethistoryattachmentsResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGethistoryExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGethistoryResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetimportantmessagesExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetimportantmessagesResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetintentusersResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetinvitelinkResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetlastactivityResponse(PydanticModel):
    response: Optional["objects.MessagesLastActivity"] = None


class MessagesGetlongpollhistoryResponse(PydanticModel):
    response: Optional[object] = None


class MessagesGetlongpollserverResponse(PydanticModel):
    response: Optional["objects.MessagesLongpollParams"] = None


class MessagesIsmessagesfromgroupallowedResponse(PydanticModel):
    response: Optional[object] = None


class MessagesJoinchatbyinvitelinkResponse(PydanticModel):
    response: Optional[object] = None


class MessagesMarkasimportantResponse(PydanticModel):
    response: Optional[List[int]] = None


class MessagesPinResponse(PydanticModel):
    response: Optional["objects.MessagesPinnedMessage"] = None


class MessagesSearchconversationsResponse(PydanticModel):
    response: Optional[object] = None


class MessagesSearchExtendedResponse(PydanticModel):
    response: Optional[object] = None


class MessagesSearchResponse(PydanticModel):
    response: Optional[object] = None


class MessagesSendResponse(PydanticModel):
    response: Optional[int] = None


class MessagesSendUserIdsResponse(PydanticModel):
    response: Optional[List[object]] = None


class MessagesSetchatphotoResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetbannedExtendedResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetbannedResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetlistsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetlistsResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetmentionsResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetrecommendedResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetsuggestedsourcesResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedGetResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedSavelistResponse(PydanticModel):
    response: Optional[int] = None


class NewsfeedSearchExtendedResponse(PydanticModel):
    response: Optional[object] = None


class NewsfeedSearchResponse(PydanticModel):
    response: Optional[object] = None


class NotesAddResponse(PydanticModel):
    response: Optional[int] = None


class NotesCreatecommentResponse(PydanticModel):
    response: Optional[int] = None


class NotesGetbyidResponse(PydanticModel):
    response: Optional["objects.NotesNote"] = None


class NotesGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class NotesGetResponse(PydanticModel):
    response: Optional[object] = None


class NotificationsGetResponse(PydanticModel):
    response: Optional[object] = None


class NotificationsMarkasviewedResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class NotificationsSendmessageResponse(PydanticModel):
    response: Optional[List["objects.NotificationsSendMessageItem"]] = None


class OrdersCancelsubscriptionResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class OrdersChangestateResponse(PydanticModel):
    response: Optional[str] = None


class OrdersGetamountResponse(PydanticModel):
    response: Optional["objects.OrdersAmount"] = None


class OrdersGetbyidResponse(PydanticModel):
    response: Optional[List["objects.OrdersOrder"]] = None


class OrdersGetusersubscriptionbyidResponse(PydanticModel):
    response: Optional["objects.OrdersSubscription"] = None


class OrdersGetusersubscriptionsResponse(PydanticModel):
    response: Optional[object] = None


class OrdersGetResponse(PydanticModel):
    response: Optional[List["objects.OrdersOrder"]] = None


class OrdersUpdatesubscriptionResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class PagesGethistoryResponse(PydanticModel):
    response: Optional[List["objects.PagesWikipageHistory"]] = None


class PagesGettitlesResponse(PydanticModel):
    response: Optional[List["objects.PagesWikipage"]] = None


class PagesGetversionResponse(PydanticModel):
    response: Optional["objects.PagesWikipageFull"] = None


class PagesGetResponse(PydanticModel):
    response: Optional["objects.PagesWikipageFull"] = None


class PagesParsewikiResponse(PydanticModel):
    response: Optional[str] = None


class PagesSaveaccessResponse(PydanticModel):
    response: Optional[int] = None


class PagesSaveResponse(PydanticModel):
    response: Optional[int] = None


class PhotosCopyResponse(PydanticModel):
    response: Optional[int] = None


class PhotosCreatealbumResponse(PydanticModel):
    response: Optional["objects.PhotosPhotoAlbumFull"] = None


class PhotosCreatecommentResponse(PydanticModel):
    response: Optional[int] = None


class PhotosDeletecommentResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class PhotosGetalbumscountResponse(PydanticModel):
    response: Optional[int] = None


class PhotosGetalbumsResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetallcommentsResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetallExtendedResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetallResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetbyidExtendedResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhotoFull"]] = None


class PhotosGetbyidResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhoto"]] = None


class PhotosGetcommentsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetmarketuploadserverResponse(PydanticModel):
    response: Optional["objects.BaseUploadServer"] = None


class PhotosGetmessagesuploadserverResponse(PydanticModel):
    response: Optional["objects.PhotosPhotoUpload"] = None


class PhotosGetnewtagsResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGettagsResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhotoTag"]] = None


class PhotosGetuploadserverResponse(PydanticModel):
    response: Optional["objects.PhotosPhotoUpload"] = None


class PhotosGetuserphotosExtendedResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetuserphotosResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetwalluploadserverResponse(PydanticModel):
    response: Optional["objects.PhotosPhotoUpload"] = None


class PhotosGetExtendedResponse(PydanticModel):
    response: Optional[object] = None


class PhotosGetResponse(PydanticModel):
    response: Optional[object] = None


class PhotosPuttagResponse(PydanticModel):
    response: Optional[int] = None


class PhotosRestorecommentResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class PhotosSavemarketalbumphotoResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhoto"]] = None


class PhotosSavemarketphotoResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhoto"]] = None


class PhotosSavemessagesphotoResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhoto"]] = None


class PhotosSaveownercoverphotoResponse(PydanticModel):
    response: Optional[List["objects.BaseImage"]] = None


class PhotosSaveownerphotoResponse(PydanticModel):
    response: Optional[object] = None


class PhotosSavewallphotoResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhoto"]] = None


class PhotosSaveResponse(PydanticModel):
    response: Optional[List["objects.PhotosPhoto"]] = None


class PhotosSearchResponse(PydanticModel):
    response: Optional[object] = None


class PollsAddvoteResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class PollsCreateResponse(PydanticModel):
    response: Optional["objects.PollsPoll"] = None


class PollsDeletevoteResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class PollsGetbackgroundsResponse(PydanticModel):
    response: Optional[List["objects.PollsBackground"]] = None


class PollsGetbyidResponse(PydanticModel):
    response: Optional["objects.PollsPoll"] = None


class PollsGetvotersResponse(PydanticModel):
    response: Optional[List["objects.PollsVoters"]] = None


class PollsSavephotoResponse(PydanticModel):
    response: Optional["objects.PollsBackground"] = None


class PrettycardsCreateResponse(PydanticModel):
    response: Optional[object] = None


class PrettycardsDeleteResponse(PydanticModel):
    response: Optional[object] = None


class PrettycardsEditResponse(PydanticModel):
    response: Optional[object] = None


class PrettycardsGetbyidResponse(PydanticModel):
    response: Optional[List["objects.PrettycardsPrettycard"]] = None


class PrettycardsGetuploadurlResponse(PydanticModel):
    response: Optional[str] = None


class PrettycardsGetResponse(PydanticModel):
    response: Optional[object] = None


class SearchGethintsResponse(PydanticModel):
    response: Optional[object] = None


class SecureChecktokenResponse(PydanticModel):
    response: Optional["objects.SecureTokenChecked"] = None


class SecureGetappbalanceResponse(PydanticModel):
    response: Optional[int] = None


class SecureGetsmshistoryResponse(PydanticModel):
    response: Optional[List["objects.SecureSmsNotification"]] = None


class SecureGettransactionshistoryResponse(PydanticModel):
    response: Optional[List["objects.SecureTransaction"]] = None


class SecureGetuserlevelResponse(PydanticModel):
    response: Optional[List["objects.SecureLevel"]] = None


class SecureGiveeventstickerResponse(PydanticModel):
    response: Optional[List[object]] = None


class SecureSendnotificationResponse(PydanticModel):
    response: Optional[List[int]] = None


class StatsGetpostreachResponse(PydanticModel):
    response: Optional[List["objects.StatsWallpostStat"]] = None


class StatsGetResponse(PydanticModel):
    response: Optional[List["objects.StatsPeriod"]] = None


class StatusGetResponse(PydanticModel):
    response: Optional["objects.StatusStatus"] = None


class StorageGetkeysResponse(PydanticModel):
    response: Optional[List[str]] = None


class StorageGetResponse(PydanticModel):
    response: Optional[List["objects.StorageValue"]] = None


class StoreGetfavoritestickersResponse(PydanticModel):
    response: Optional[List["objects.BaseSticker"]] = None


class StoreGetproductsResponse(PydanticModel):
    response: Optional[List["objects.StoreProduct"]] = None


class StoreGetstickerskeywordsResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetbannedExtendedResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetbannedResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetbyidExtendedResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetbyidResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetphotouploadserverResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetstatsResponse(PydanticModel):
    response: Optional["objects.StoriesStoryStats"] = None


class StoriesGetvideouploadserverResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetviewersExtendedV5115Response(PydanticModel):
    response: Optional[object] = None


class StoriesGetviewersExtendedResponse(PydanticModel):
    response: Optional[object] = None


class StoriesGetV5113Response(PydanticModel):
    response: Optional[object] = None


class StoriesGetResponse(PydanticModel):
    response: Optional[object] = None


class StoriesSaveResponse(PydanticModel):
    response: Optional[object] = None


class StoriesUploadResponse(PydanticModel):
    response: Optional[object] = None


class StreamingGetserverurlResponse(PydanticModel):
    response: Optional[object] = None


class UsersGetfollowersFieldsResponse(PydanticModel):
    response: Optional[object] = None


class UsersGetfollowersResponse(PydanticModel):
    response: Optional[object] = None


class UsersGetsubscriptionsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class UsersGetsubscriptionsResponse(PydanticModel):
    response: Optional[object] = None


class UsersGetResponse(PydanticModel):
    response: Optional[List["objects.UsersUserXtrCounters"]] = None


class UsersSearchResponse(PydanticModel):
    response: Optional[object] = None


class UtilsChecklinkResponse(PydanticModel):
    response: Optional["objects.UtilsLinkChecked"] = None


class UtilsGetlastshortenedlinksResponse(PydanticModel):
    response: Optional[object] = None


class UtilsGetlinkstatsExtendedResponse(PydanticModel):
    response: Optional["objects.UtilsLinkStatsExtended"] = None


class UtilsGetlinkstatsResponse(PydanticModel):
    response: Optional["objects.UtilsLinkStats"] = None


class UtilsGetservertimeResponse(PydanticModel):
    response: Optional[int] = None


class UtilsGetshortlinkResponse(PydanticModel):
    response: Optional["objects.UtilsShortLink"] = None


class UtilsResolvescreennameResponse(PydanticModel):
    response: Optional["objects.UtilsDomainResolved"] = None


class VideoAddalbumResponse(PydanticModel):
    response: Optional[object] = None


class VideoCreatecommentResponse(PydanticModel):
    response: Optional[int] = None


class VideoGetalbumbyidResponse(PydanticModel):
    response: Optional["objects.VideoVideoAlbumFull"] = None


class VideoGetalbumsbyvideoExtendedResponse(PydanticModel):
    response: Optional[object] = None


class VideoGetalbumsbyvideoResponse(PydanticModel):
    response: Optional[List[int]] = None


class VideoGetalbumsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class VideoGetalbumsResponse(PydanticModel):
    response: Optional[object] = None


class VideoGetcommentsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class VideoGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class VideoGetExtendedResponse(PydanticModel):
    response: Optional[object] = None


class VideoGetResponse(PydanticModel):
    response: Optional[object] = None


class VideoRestorecommentResponse(PydanticModel):
    response: Optional["objects.BaseBoolInt"] = None


class VideoSaveResponse(PydanticModel):
    response: Optional["objects.VideoSaveResult"] = None


class VideoSearchExtendedResponse(PydanticModel):
    response: Optional[object] = None


class VideoSearchResponse(PydanticModel):
    response: Optional[object] = None


class WallCreatecommentResponse(PydanticModel):
    response: Optional[object] = None


class WallEditResponse(PydanticModel):
    response: Optional[object] = None


class WallGetbyidExtendedResponse(PydanticModel):
    response: Optional[object] = None


class WallGetbyidLegacyResponse(PydanticModel):
    response: Optional[List["objects.WallWallpostFull"]] = None


class WallGetbyidResponse(PydanticModel):
    response: Optional[object] = None


class WallGetcommentExtendedResponse(PydanticModel):
    response: Optional[object] = None


class WallGetcommentResponse(PydanticModel):
    response: Optional[object] = None


class WallGetcommentsExtendedResponse(PydanticModel):
    response: Optional[object] = None


class WallGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class WallGetrepostsResponse(PydanticModel):
    response: Optional[object] = None


class WallGetExtendedResponse(PydanticModel):
    response: Optional[object] = None


class WallGetResponse(PydanticModel):
    response: Optional[object] = None


class WallPostadsstealthResponse(PydanticModel):
    response: Optional[object] = None


class WallPostResponse(PydanticModel):
    response: Optional[object] = None


class WallRepostResponse(PydanticModel):
    response: Optional[object] = None


class WallSearchExtendedResponse(PydanticModel):
    response: Optional[object] = None


class WallSearchResponse(PydanticModel):
    response: Optional[object] = None


class WidgetsGetcommentsResponse(PydanticModel):
    response: Optional[object] = None


class WidgetsGetpagesResponse(PydanticModel):
    response: Optional[object] = None


AccountChangepasswordResponse.update_forward_refs()
AccountGetactiveoffersResponse.update_forward_refs()
AccountGetapppermissionsResponse.update_forward_refs()
AccountGetbannedResponse.update_forward_refs()
AccountGetcountersResponse.update_forward_refs()
AccountGetinfoResponse.update_forward_refs()
AccountGetprofileinfoResponse.update_forward_refs()
AccountGetpushsettingsResponse.update_forward_refs()
AccountSaveprofileinfoResponse.update_forward_refs()
AdsAddofficeusersResponse.update_forward_refs()
AdsChecklinkResponse.update_forward_refs()
AdsCreateadsResponse.update_forward_refs()
AdsCreatecampaignsResponse.update_forward_refs()
AdsCreateclientsResponse.update_forward_refs()
AdsCreatetargetgroupResponse.update_forward_refs()
AdsDeleteadsResponse.update_forward_refs()
AdsDeletecampaignsResponse.update_forward_refs()
AdsDeleteclientsResponse.update_forward_refs()
AdsGetaccountsResponse.update_forward_refs()
AdsGetadslayoutResponse.update_forward_refs()
AdsGetadstargetingResponse.update_forward_refs()
AdsGetadsResponse.update_forward_refs()
AdsGetbudgetResponse.update_forward_refs()
AdsGetcampaignsResponse.update_forward_refs()
AdsGetcategoriesResponse.update_forward_refs()
AdsGetclientsResponse.update_forward_refs()
AdsGetdemographicsResponse.update_forward_refs()
AdsGetfloodstatsResponse.update_forward_refs()
AdsGetlookalikerequestsResponse.update_forward_refs()
AdsGetmusiciansResponse.update_forward_refs()
AdsGetofficeusersResponse.update_forward_refs()
AdsGetpostsreachResponse.update_forward_refs()
AdsGetrejectionreasonResponse.update_forward_refs()
AdsGetstatisticsResponse.update_forward_refs()
AdsGetsuggestionsCitiesResponse.update_forward_refs()
AdsGetsuggestionsRegionsResponse.update_forward_refs()
AdsGetsuggestionsResponse.update_forward_refs()
AdsGetsuggestionsSchoolsResponse.update_forward_refs()
AdsGettargetgroupsResponse.update_forward_refs()
AdsGettargetingstatsResponse.update_forward_refs()
AdsGetuploadurlResponse.update_forward_refs()
AdsGetvideouploadurlResponse.update_forward_refs()
AdsImporttargetcontactsResponse.update_forward_refs()
AdsRemoveofficeusersResponse.update_forward_refs()
AdsUpdateadsResponse.update_forward_refs()
AdsUpdatecampaignsResponse.update_forward_refs()
AdsUpdateclientsResponse.update_forward_refs()
AdsUpdateofficeusersResponse.update_forward_refs()
AdswebGetadcategoriesResponse.update_forward_refs()
AdswebGetadunitcodeResponse.update_forward_refs()
AdswebGetadunitsResponse.update_forward_refs()
AdswebGetfraudhistoryResponse.update_forward_refs()
AdswebGetsitesResponse.update_forward_refs()
AdswebGetstatisticsResponse.update_forward_refs()
AppwidgetsGetappimageuploadserverResponse.update_forward_refs()
AppwidgetsGetappimagesResponse.update_forward_refs()
AppwidgetsGetgroupimageuploadserverResponse.update_forward_refs()
AppwidgetsGetgroupimagesResponse.update_forward_refs()
AppwidgetsGetimagesbyidResponse.update_forward_refs()
AppwidgetsSaveappimageResponse.update_forward_refs()
AppwidgetsSavegroupimageResponse.update_forward_refs()
AppsGetcatalogResponse.update_forward_refs()
AppsGetfriendslistResponse.update_forward_refs()
AppsGetleaderboardExtendedResponse.update_forward_refs()
AppsGetleaderboardResponse.update_forward_refs()
AppsGetscopesResponse.update_forward_refs()
AppsGetscoreResponse.update_forward_refs()
AppsGetResponse.update_forward_refs()
AppsSendrequestResponse.update_forward_refs()
AuthRestoreResponse.update_forward_refs()
BaseBoolResponse.update_forward_refs()
BaseGetuploadserverResponse.update_forward_refs()
BaseOkResponse.update_forward_refs()
BoardAddtopicResponse.update_forward_refs()
BoardCreatecommentResponse.update_forward_refs()
BoardGetcommentsExtendedResponse.update_forward_refs()
BoardGetcommentsResponse.update_forward_refs()
BoardGettopicsExtendedResponse.update_forward_refs()
BoardGettopicsResponse.update_forward_refs()
DatabaseGetchairsResponse.update_forward_refs()
DatabaseGetcitiesbyidResponse.update_forward_refs()
DatabaseGetcitiesResponse.update_forward_refs()
DatabaseGetcountriesbyidResponse.update_forward_refs()
DatabaseGetcountriesResponse.update_forward_refs()
DatabaseGetfacultiesResponse.update_forward_refs()
DatabaseGetmetrostationsbyidResponse.update_forward_refs()
DatabaseGetmetrostationsResponse.update_forward_refs()
DatabaseGetregionsResponse.update_forward_refs()
DatabaseGetschoolclassesResponse.update_forward_refs()
DatabaseGetschoolsResponse.update_forward_refs()
DatabaseGetuniversitiesResponse.update_forward_refs()
DocsAddResponse.update_forward_refs()
DocsGetbyidResponse.update_forward_refs()
DocsGettypesResponse.update_forward_refs()
DocsGetuploadserver.update_forward_refs()
DocsGetResponse.update_forward_refs()
DocsSaveResponse.update_forward_refs()
DocsSearchResponse.update_forward_refs()
DonutGetsubscriptionResponse.update_forward_refs()
DonutGetsubscriptionsResponse.update_forward_refs()
DownloadedgamesPaidStatusResponse.update_forward_refs()
FaveAddtagResponse.update_forward_refs()
FaveGetpagesResponse.update_forward_refs()
FaveGettagsResponse.update_forward_refs()
FaveGetExtendedResponse.update_forward_refs()
FaveGetResponse.update_forward_refs()
FriendsAddlistResponse.update_forward_refs()
FriendsAddResponse.update_forward_refs()
FriendsArefriendsExtendedResponse.update_forward_refs()
FriendsArefriendsResponse.update_forward_refs()
FriendsDeleteResponse.update_forward_refs()
FriendsGetappusersResponse.update_forward_refs()
FriendsGetbyphonesResponse.update_forward_refs()
FriendsGetlistsResponse.update_forward_refs()
FriendsGetmutualResponse.update_forward_refs()
FriendsGetmutualTargetUidsResponse.update_forward_refs()
FriendsGetonlineOnlineMobileResponse.update_forward_refs()
FriendsGetonlineResponse.update_forward_refs()
FriendsGetrecentResponse.update_forward_refs()
FriendsGetrequestsExtendedResponse.update_forward_refs()
FriendsGetrequestsNeedMutualResponse.update_forward_refs()
FriendsGetrequestsResponse.update_forward_refs()
FriendsGetsuggestionsResponse.update_forward_refs()
FriendsGetFieldsResponse.update_forward_refs()
FriendsGetResponse.update_forward_refs()
FriendsSearchResponse.update_forward_refs()
GiftsGetResponse.update_forward_refs()
GroupsAddaddressResponse.update_forward_refs()
GroupsAddcallbackserverResponse.update_forward_refs()
GroupsAddlinkResponse.update_forward_refs()
GroupsCreateResponse.update_forward_refs()
GroupsEditaddressResponse.update_forward_refs()
GroupsGetaddressesResponse.update_forward_refs()
GroupsGetbannedResponse.update_forward_refs()
GroupsGetbyidLegacyResponse.update_forward_refs()
GroupsGetbyidResponse.update_forward_refs()
GroupsGetcallbackconfirmationcodeResponse.update_forward_refs()
GroupsGetcallbackserversResponse.update_forward_refs()
GroupsGetcallbacksettingsResponse.update_forward_refs()
GroupsGetcataloginfoExtendedResponse.update_forward_refs()
GroupsGetcataloginfoResponse.update_forward_refs()
GroupsGetcatalogResponse.update_forward_refs()
GroupsGetinvitedusersResponse.update_forward_refs()
GroupsGetinvitesExtendedResponse.update_forward_refs()
GroupsGetinvitesResponse.update_forward_refs()
GroupsGetlongpollserverResponse.update_forward_refs()
GroupsGetlongpollsettingsResponse.update_forward_refs()
GroupsGetmembersFieldsResponse.update_forward_refs()
GroupsGetmembersFilterResponse.update_forward_refs()
GroupsGetmembersResponse.update_forward_refs()
GroupsGetrequestsFieldsResponse.update_forward_refs()
GroupsGetrequestsResponse.update_forward_refs()
GroupsGetsettingsResponse.update_forward_refs()
GroupsGettaglistResponse.update_forward_refs()
GroupsGettokenpermissionsResponse.update_forward_refs()
GroupsGetExtendedResponse.update_forward_refs()
GroupsGetResponse.update_forward_refs()
GroupsIsmemberExtendedResponse.update_forward_refs()
GroupsIsmemberResponse.update_forward_refs()
GroupsIsmemberUserIdsExtendedResponse.update_forward_refs()
GroupsIsmemberUserIdsResponse.update_forward_refs()
GroupsSearchResponse.update_forward_refs()
LikesAddResponse.update_forward_refs()
LikesDeleteResponse.update_forward_refs()
LikesGetlistExtendedResponse.update_forward_refs()
LikesGetlistResponse.update_forward_refs()
LikesIslikedResponse.update_forward_refs()
MarketAddalbumResponse.update_forward_refs()
MarketAddResponse.update_forward_refs()
MarketCreatecommentResponse.update_forward_refs()
MarketDeletecommentResponse.update_forward_refs()
MarketGetalbumbyidResponse.update_forward_refs()
MarketGetalbumsResponse.update_forward_refs()
MarketGetbyidExtendedResponse.update_forward_refs()
MarketGetbyidResponse.update_forward_refs()
MarketGetcategoriesNewResponse.update_forward_refs()
MarketGetcategoriesResponse.update_forward_refs()
MarketGetcommentsResponse.update_forward_refs()
MarketGetgroupordersResponse.update_forward_refs()
MarketGetorderbyidResponse.update_forward_refs()
MarketGetorderitemsResponse.update_forward_refs()
MarketGetordersExtendedResponse.update_forward_refs()
MarketGetordersResponse.update_forward_refs()
MarketGetExtendedResponse.update_forward_refs()
MarketGetResponse.update_forward_refs()
MarketRestorecommentResponse.update_forward_refs()
MarketSearchExtendedResponse.update_forward_refs()
MarketSearchResponse.update_forward_refs()
MessagesCreatechatResponse.update_forward_refs()
MessagesDeletechatphotoResponse.update_forward_refs()
MessagesDeleteconversationResponse.update_forward_refs()
MessagesDeleteResponse.update_forward_refs()
MessagesEditResponse.update_forward_refs()
MessagesGetbyconversationmessageidResponse.update_forward_refs()
MessagesGetbyidExtendedResponse.update_forward_refs()
MessagesGetbyidResponse.update_forward_refs()
MessagesGetchatpreviewResponse.update_forward_refs()
MessagesGetchatChatIdsFieldsResponse.update_forward_refs()
MessagesGetchatChatIdsResponse.update_forward_refs()
MessagesGetchatFieldsResponse.update_forward_refs()
MessagesGetchatResponse.update_forward_refs()
MessagesGetconversationmembersResponse.update_forward_refs()
MessagesGetconversationsbyidExtendedResponse.update_forward_refs()
MessagesGetconversationsbyidResponse.update_forward_refs()
MessagesGetconversationsResponse.update_forward_refs()
MessagesGethistoryattachmentsResponse.update_forward_refs()
MessagesGethistoryExtendedResponse.update_forward_refs()
MessagesGethistoryResponse.update_forward_refs()
MessagesGetimportantmessagesExtendedResponse.update_forward_refs()
MessagesGetimportantmessagesResponse.update_forward_refs()
MessagesGetintentusersResponse.update_forward_refs()
MessagesGetinvitelinkResponse.update_forward_refs()
MessagesGetlastactivityResponse.update_forward_refs()
MessagesGetlongpollhistoryResponse.update_forward_refs()
MessagesGetlongpollserverResponse.update_forward_refs()
MessagesIsmessagesfromgroupallowedResponse.update_forward_refs()
MessagesJoinchatbyinvitelinkResponse.update_forward_refs()
MessagesMarkasimportantResponse.update_forward_refs()
MessagesPinResponse.update_forward_refs()
MessagesSearchconversationsResponse.update_forward_refs()
MessagesSearchExtendedResponse.update_forward_refs()
MessagesSearchResponse.update_forward_refs()
MessagesSendResponse.update_forward_refs()
MessagesSendUserIdsResponse.update_forward_refs()
MessagesSetchatphotoResponse.update_forward_refs()
NewsfeedGetbannedExtendedResponse.update_forward_refs()
NewsfeedGetbannedResponse.update_forward_refs()
NewsfeedGetcommentsResponse.update_forward_refs()
NewsfeedGetlistsExtendedResponse.update_forward_refs()
NewsfeedGetlistsResponse.update_forward_refs()
NewsfeedGetmentionsResponse.update_forward_refs()
NewsfeedGetrecommendedResponse.update_forward_refs()
NewsfeedGetsuggestedsourcesResponse.update_forward_refs()
NewsfeedGetResponse.update_forward_refs()
NewsfeedSavelistResponse.update_forward_refs()
NewsfeedSearchExtendedResponse.update_forward_refs()
NewsfeedSearchResponse.update_forward_refs()
NotesAddResponse.update_forward_refs()
NotesCreatecommentResponse.update_forward_refs()
NotesGetbyidResponse.update_forward_refs()
NotesGetcommentsResponse.update_forward_refs()
NotesGetResponse.update_forward_refs()
NotificationsGetResponse.update_forward_refs()
NotificationsMarkasviewedResponse.update_forward_refs()
NotificationsSendmessageResponse.update_forward_refs()
OrdersCancelsubscriptionResponse.update_forward_refs()
OrdersChangestateResponse.update_forward_refs()
OrdersGetamountResponse.update_forward_refs()
OrdersGetbyidResponse.update_forward_refs()
OrdersGetusersubscriptionbyidResponse.update_forward_refs()
OrdersGetusersubscriptionsResponse.update_forward_refs()
OrdersGetResponse.update_forward_refs()
OrdersUpdatesubscriptionResponse.update_forward_refs()
PagesGethistoryResponse.update_forward_refs()
PagesGettitlesResponse.update_forward_refs()
PagesGetversionResponse.update_forward_refs()
PagesGetResponse.update_forward_refs()
PagesParsewikiResponse.update_forward_refs()
PagesSaveaccessResponse.update_forward_refs()
PagesSaveResponse.update_forward_refs()
PhotosCopyResponse.update_forward_refs()
PhotosCreatealbumResponse.update_forward_refs()
PhotosCreatecommentResponse.update_forward_refs()
PhotosDeletecommentResponse.update_forward_refs()
PhotosGetalbumscountResponse.update_forward_refs()
PhotosGetalbumsResponse.update_forward_refs()
PhotosGetallcommentsResponse.update_forward_refs()
PhotosGetallExtendedResponse.update_forward_refs()
PhotosGetallResponse.update_forward_refs()
PhotosGetbyidExtendedResponse.update_forward_refs()
PhotosGetbyidResponse.update_forward_refs()
PhotosGetcommentsExtendedResponse.update_forward_refs()
PhotosGetcommentsResponse.update_forward_refs()
PhotosGetmarketuploadserverResponse.update_forward_refs()
PhotosGetmessagesuploadserverResponse.update_forward_refs()
PhotosGetnewtagsResponse.update_forward_refs()
PhotosGettagsResponse.update_forward_refs()
PhotosGetuploadserverResponse.update_forward_refs()
PhotosGetuserphotosExtendedResponse.update_forward_refs()
PhotosGetuserphotosResponse.update_forward_refs()
PhotosGetwalluploadserverResponse.update_forward_refs()
PhotosGetExtendedResponse.update_forward_refs()
PhotosGetResponse.update_forward_refs()
PhotosPuttagResponse.update_forward_refs()
PhotosRestorecommentResponse.update_forward_refs()
PhotosSavemarketalbumphotoResponse.update_forward_refs()
PhotosSavemarketphotoResponse.update_forward_refs()
PhotosSavemessagesphotoResponse.update_forward_refs()
PhotosSaveownercoverphotoResponse.update_forward_refs()
PhotosSaveownerphotoResponse.update_forward_refs()
PhotosSavewallphotoResponse.update_forward_refs()
PhotosSaveResponse.update_forward_refs()
PhotosSearchResponse.update_forward_refs()
PollsAddvoteResponse.update_forward_refs()
PollsCreateResponse.update_forward_refs()
PollsDeletevoteResponse.update_forward_refs()
PollsGetbackgroundsResponse.update_forward_refs()
PollsGetbyidResponse.update_forward_refs()
PollsGetvotersResponse.update_forward_refs()
PollsSavephotoResponse.update_forward_refs()
PrettycardsCreateResponse.update_forward_refs()
PrettycardsDeleteResponse.update_forward_refs()
PrettycardsEditResponse.update_forward_refs()
PrettycardsGetbyidResponse.update_forward_refs()
PrettycardsGetuploadurlResponse.update_forward_refs()
PrettycardsGetResponse.update_forward_refs()
SearchGethintsResponse.update_forward_refs()
SecureChecktokenResponse.update_forward_refs()
SecureGetappbalanceResponse.update_forward_refs()
SecureGetsmshistoryResponse.update_forward_refs()
SecureGettransactionshistoryResponse.update_forward_refs()
SecureGetuserlevelResponse.update_forward_refs()
SecureGiveeventstickerResponse.update_forward_refs()
SecureSendnotificationResponse.update_forward_refs()
StatsGetpostreachResponse.update_forward_refs()
StatsGetResponse.update_forward_refs()
StatusGetResponse.update_forward_refs()
StorageGetkeysResponse.update_forward_refs()
StorageGetResponse.update_forward_refs()
StoreGetfavoritestickersResponse.update_forward_refs()
StoreGetproductsResponse.update_forward_refs()
StoreGetstickerskeywordsResponse.update_forward_refs()
StoriesGetbannedExtendedResponse.update_forward_refs()
StoriesGetbannedResponse.update_forward_refs()
StoriesGetbyidExtendedResponse.update_forward_refs()
StoriesGetbyidResponse.update_forward_refs()
StoriesGetphotouploadserverResponse.update_forward_refs()
StoriesGetstatsResponse.update_forward_refs()
StoriesGetvideouploadserverResponse.update_forward_refs()
StoriesGetviewersExtendedV5115Response.update_forward_refs()
StoriesGetviewersExtendedResponse.update_forward_refs()
StoriesGetV5113Response.update_forward_refs()
StoriesGetResponse.update_forward_refs()
StoriesSaveResponse.update_forward_refs()
StoriesUploadResponse.update_forward_refs()
StreamingGetserverurlResponse.update_forward_refs()
UsersGetfollowersFieldsResponse.update_forward_refs()
UsersGetfollowersResponse.update_forward_refs()
UsersGetsubscriptionsExtendedResponse.update_forward_refs()
UsersGetsubscriptionsResponse.update_forward_refs()
UsersGetResponse.update_forward_refs()
UsersSearchResponse.update_forward_refs()
UtilsChecklinkResponse.update_forward_refs()
UtilsGetlastshortenedlinksResponse.update_forward_refs()
UtilsGetlinkstatsExtendedResponse.update_forward_refs()
UtilsGetlinkstatsResponse.update_forward_refs()
UtilsGetservertimeResponse.update_forward_refs()
UtilsGetshortlinkResponse.update_forward_refs()
UtilsResolvescreennameResponse.update_forward_refs()
VideoAddalbumResponse.update_forward_refs()
VideoCreatecommentResponse.update_forward_refs()
VideoGetalbumbyidResponse.update_forward_refs()
VideoGetalbumsbyvideoExtendedResponse.update_forward_refs()
VideoGetalbumsbyvideoResponse.update_forward_refs()
VideoGetalbumsExtendedResponse.update_forward_refs()
VideoGetalbumsResponse.update_forward_refs()
VideoGetcommentsExtendedResponse.update_forward_refs()
VideoGetcommentsResponse.update_forward_refs()
VideoGetExtendedResponse.update_forward_refs()
VideoGetResponse.update_forward_refs()
VideoRestorecommentResponse.update_forward_refs()
VideoSaveResponse.update_forward_refs()
VideoSearchExtendedResponse.update_forward_refs()
VideoSearchResponse.update_forward_refs()
WallCreatecommentResponse.update_forward_refs()
WallEditResponse.update_forward_refs()
WallGetbyidExtendedResponse.update_forward_refs()
WallGetbyidLegacyResponse.update_forward_refs()
WallGetbyidResponse.update_forward_refs()
WallGetcommentExtendedResponse.update_forward_refs()
WallGetcommentResponse.update_forward_refs()
WallGetcommentsExtendedResponse.update_forward_refs()
WallGetcommentsResponse.update_forward_refs()
WallGetrepostsResponse.update_forward_refs()
WallGetExtendedResponse.update_forward_refs()
WallGetResponse.update_forward_refs()
WallPostadsstealthResponse.update_forward_refs()
WallPostResponse.update_forward_refs()
WallRepostResponse.update_forward_refs()
WallSearchExtendedResponse.update_forward_refs()
WallSearchResponse.update_forward_refs()
WidgetsGetcommentsResponse.update_forward_refs()
WidgetsGetpagesResponse.update_forward_refs()