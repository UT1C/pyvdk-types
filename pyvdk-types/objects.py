from typing import Optional, Union, Any, List, Tuple
import enum

from pydantic import BaseModel as PydanticModel


class AccountAccountCounters(PydanticModel):
    app_requests: int
    events: int
    faves: int
    friends: int
    friends_suggestions: int
    friends_recommendations: int
    gifts: int
    groups: int
    menu_discover_badge: int
    menu_clips_badge: int
    messages: int
    memories: int
    notes: int
    notifications: int
    photos: int
    sdk: int


class AccountInfo(PydanticModel):
    wishlists_ae_promo_banner_show: "BaseBoolInt"
    _2fa_required: "BaseBoolInt"
    country: str
    https_required: "BaseBoolInt"
    intro: "BaseBoolInt"
    show_vk_apps_intro: bool
    mini_apps_ads_slot_id: int
    qr_promotion: int
    link_redirects: object
    lang: int
    no_wall_replies: "BaseBoolInt"
    own_posts_default: "BaseBoolInt"
    subscriptions: List[int]


class AccountNameRequest(PydanticModel):
    first_name: str
    id: int
    last_name: str
    status: "AccountNameRequestStatus"
    lang: str
    link_href: str
    link_label: str


class AccountNameRequestStatus(enum.Enum):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class AccountOffer(PydanticModel):
    description: str
    id: int
    img: str
    instruction: str
    instruction_html: str
    price: int
    short_description: str
    tag: str
    title: str
    currency_amount: int
    link_id: int
    link_type: str


class AccountPushConversations(PydanticModel):
    count: int
    items: List["AccountPushConversationsItem"]


class AccountPushConversationsItem(PydanticModel):
    disabled_until: int
    peer_id: int
    sound: "BaseBoolInt"


class AccountPushParams(PydanticModel):
    msg: List["AccountPushParamsMode"]
    chat: List["AccountPushParamsMode"]
    like: List["AccountPushParamsSettings"]
    repost: List["AccountPushParamsSettings"]
    comment: List["AccountPushParamsSettings"]
    mention: List["AccountPushParamsSettings"]
    reply: List["AccountPushParamsOnoff"]
    new_post: List["AccountPushParamsOnoff"]
    wall_post: List["AccountPushParamsOnoff"]
    wall_publish: List["AccountPushParamsOnoff"]
    friend: List["AccountPushParamsOnoff"]
    friend_found: List["AccountPushParamsOnoff"]
    friend_accepted: List["AccountPushParamsOnoff"]
    group_invite: List["AccountPushParamsOnoff"]
    group_accepted: List["AccountPushParamsOnoff"]
    birthday: List["AccountPushParamsOnoff"]
    event_soon: List["AccountPushParamsOnoff"]
    app_request: List["AccountPushParamsOnoff"]
    sdk_open: List["AccountPushParamsOnoff"]


class AccountPushParamsMode(enum.Enum):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class AccountPushParamsOnoff(enum.Enum):
    ON = "on"
    OFF = "off"


class AccountPushParamsSettings(enum.Enum):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"


class AccountPushSettings(PydanticModel):
    disabled: "BaseBoolInt"
    disabled_until: int
    settings: "AccountPushParams"
    conversations: "AccountPushConversations"


class AccountUserSettings(PydanticModel):
    allOf: Unsupported


class AccountUserSettingsInterest(PydanticModel):
    title: str
    value: str


class AccountUserSettingsInterests(PydanticModel):
    activities: "AccountUserSettingsInterest"
    interests: "AccountUserSettingsInterest"
    music: "AccountUserSettingsInterest"
    tv: "AccountUserSettingsInterest"
    movies: "AccountUserSettingsInterest"
    books: "AccountUserSettingsInterest"
    games: "AccountUserSettingsInterest"
    quotes: "AccountUserSettingsInterest"
    about: "AccountUserSettingsInterest"


class AddressesFields(enum.Enum):
    ID = "id"
    TITLE = "title"
    ADDRESS = "address"
    ADDITIONAL_ADDRESS = "additional_address"
    COUNTRY_ID = "country_id"
    CITY_ID = "city_id"
    METRO_STATION_ID = "metro_station_id"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    DISTANCE = "distance"
    WORK_INFO_STATUS = "work_info_status"
    TIMETABLE = "timetable"
    PHONE = "phone"
    TIME_OFFSET = "time_offset"


class AdsAccessRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccessRolePublic(enum.Enum):
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccesses(PydanticModel):
    client_id: str
    role: "AdsAccessRole"


class AdsAccount(PydanticModel):
    access_role: "AdsAccessRole"
    account_id: int
    account_status: "BaseBoolInt"
    account_type: "AdsAccountType"
    account_name: str
    can_view_budget: bool


class AdsAccountType(enum.Enum):
    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(PydanticModel):
    ad_format: int
    ad_platform: Union[int, str]
    all_limit: int
    approved: "AdsAdApproved"
    campaign_id: int
    category1_id: int
    category2_id: int
    cost_type: "AdsAdCostType"
    cpc: int
    cpm: int
    cpa: int
    ocpm: int
    autobidding_max_cost: int
    disclaimer_medical: "BaseBoolInt"
    disclaimer_specialist: "BaseBoolInt"
    disclaimer_supplements: "BaseBoolInt"
    id: int
    impressions_limit: int
    impressions_limited: "BaseBoolInt"
    name: str
    status: "AdsAdStatus"
    video: "BaseBoolInt"


class AdsAdApproved(enum.IntEnum):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdsAdCostType(enum.IntEnum):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdLayout(PydanticModel):
    ad_format: int
    campaign_id: int
    cost_type: "AdsAdCostType"
    description: str
    id: str
    image_src: str
    image_src_2x: str
    link_domain: str
    link_url: str
    preview_link: Union[int, str]
    title: str
    video: "BaseBoolInt"


class AdsAdStatus(enum.IntEnum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaign(PydanticModel):
    all_limit: str
    day_limit: str
    id: int
    name: str
    start_time: int
    status: "AdsCampaignStatus"
    stop_time: int
    type: "AdsCampaignType"


class AdsCampaignStatus(enum.IntEnum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaignType(enum.Enum):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"


class AdsCategory(PydanticModel):
    id: int
    name: str
    subcategories: List["BaseObjectWithName"]


class AdsClient(PydanticModel):
    all_limit: str
    day_limit: str
    id: int
    name: str


class AdsCriteria(PydanticModel):
    age_from: int
    age_to: int
    apps: str
    apps_not: str
    birthday: int
    cities: str
    cities_not: str
    country: int
    districts: str
    groups: str
    interest_categories: str
    interests: str
    paying: "BaseBoolInt"
    positions: str
    religions: str
    retargeting_groups: str
    retargeting_groups_not: str
    school_from: int
    school_to: int
    schools: str
    sex: "AdsCriteriaSex"
    stations: str
    statuses: str
    streets: str
    travellers: "BasePropertyExists"
    uni_from: int
    uni_to: int
    user_browsers: str
    user_devices: str
    user_os: str


class AdsCriteriaSex(enum.IntEnum):
    ANY = 0
    MALE = 1
    FEMALE = 2


class AdsDemoStats(PydanticModel):
    id: int
    stats: "AdsDemostatsFormat"
    type: "AdsObjectType"


class AdsDemostatsFormat(PydanticModel):
    age: List["AdsStatsAge"]
    cities: List["AdsStatsCities"]
    day: str
    month: str
    overall: int
    sex: List["AdsStatsSex"]
    sex_age: List["AdsStatsSexAge"]


class AdsFloodStats(PydanticModel):
    left: int
    refresh: int


class AdsLinkStatus(PydanticModel):
    description: str
    redirect_url: str
    status: str


class AdsLookalikeRequest(PydanticModel):
    id: int
    create_time: int
    update_time: int
    scheduled_delete_time: int
    status: str
    source_type: str
    source_retargeting_group_id: int
    source_name: str
    audience_count: int
    save_audience_levels: List["AdsLookalikeRequestSaveAudienceLevel"]


class AdsLookalikeRequestSaveAudienceLevel(PydanticModel):
    level: int
    audience_count: int


class AdsMusician(PydanticModel):
    id: int
    name: str


class AdsObjectType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsParagraphs(PydanticModel):
    paragraph: str


class AdsPromotedPostReach(PydanticModel):
    hide: int
    id: int
    join_group: int
    links: int
    reach_subscribers: int
    reach_total: int
    report: int
    to_group: int
    unsubscribe: int
    video_views_100p: int
    video_views_25p: int
    video_views_3s: int
    video_views_50p: int
    video_views_75p: int
    video_views_start: int


class AdsRejectReason(PydanticModel):
    comment: str
    rules: List["AdsRules"]


class AdsRules(PydanticModel):
    paragraphs: List["AdsParagraphs"]
    title: str


class AdsStats(PydanticModel):
    id: int
    stats: "AdsStatsFormat"
    type: "AdsObjectType"
    views_times: "AdsStatsViewsTimes"


class AdsStatsAge(PydanticModel):
    clicks_rate: int
    impressions_rate: int
    value: str


class AdsStatsCities(PydanticModel):
    clicks_rate: int
    impressions_rate: int
    name: str
    value: int


class AdsStatsFormat(PydanticModel):
    clicks: int
    day: str
    impressions: int
    join_rate: int
    month: str
    overall: int
    reach: int
    spent: int
    video_clicks_site: int
    video_views: int
    video_views_full: int
    video_views_half: int


class AdsStatsSex(PydanticModel):
    clicks_rate: int
    impressions_rate: int
    value: "AdsStatsSexValue"


class AdsStatsSexAge(PydanticModel):
    clicks_rate: int
    impressions_rate: int
    value: str


class AdsStatsSexValue(enum.Enum):
    F = "f"
    M = "m"


class AdsStatsViewsTimes(PydanticModel):
    views_ads_times_1: int
    views_ads_times_2: int
    views_ads_times_3: int
    views_ads_times_4: int
    views_ads_times_5: str
    views_ads_times_6: int
    views_ads_times_7: int
    views_ads_times_8: int
    views_ads_times_9: int
    views_ads_times_10: int
    views_ads_times_11_plus: int


class AdsTargSettings(PydanticModel):
    allOf: Unsupported


class AdsTargStats(PydanticModel):
    audience_count: int
    recommended_cpc: int
    recommended_cpm: int
    recommended_cpc_50: int
    recommended_cpm_50: int
    recommended_cpc_70: int
    recommended_cpm_70: int
    recommended_cpc_90: int
    recommended_cpm_90: int


class AdsTargSuggestions(PydanticModel):
    id: int
    name: str


class AdsTargSuggestionsCities(PydanticModel):
    id: int
    name: str
    parent: str


class AdsTargSuggestionsRegions(PydanticModel):
    id: int
    name: str
    type: str


class AdsTargSuggestionsSchools(PydanticModel):
    desc: str
    id: int
    name: str
    parent: str
    type: "AdsTargSuggestionsSchoolsType"


class AdsTargSuggestionsSchoolsType(enum.Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(PydanticModel):
    audience_count: int
    domain: str
    id: int
    lifetime: int
    name: str
    pixel: str


class AdsUpdateofficeusersResult(PydanticModel):
    user_id: int
    is_success: bool
    error: "BaseError"


class AdsUserSpecification(PydanticModel):
    user_id: int
    role: "AdsAccessRolePublic"
    grant_access_to_all_clients: bool
    client_ids: List[int]
    view_budget: bool


class AdsUserSpecificationCutted(PydanticModel):
    user_id: int
    role: "AdsAccessRolePublic"
    client_id: int
    view_budget: bool


class AdsUsers(PydanticModel):
    accesses: List["AdsAccesses"]
    user_id: int


class AdswebGetadcategoriesResponseCategoriesCategory(PydanticModel):
    id: int
    name: str


class AdswebGetadunitsResponseAdUnitsAdUnit(PydanticModel):
    id: int
    site_id: int
    name: str


class AdswebGetfraudhistoryResponseEntriesEntry(PydanticModel):
    site_id: int
    day: str


class AdswebGetsitesResponseSitesSite(PydanticModel):
    id: int
    status_user: str
    status_moder: str
    domains: str


class AdswebGetstatisticsResponseItemsItem(PydanticModel):
    site_id: int
    ad_unit_id: int
    overall_count: int
    months_count: int
    month_min: str
    month_max: str
    days_count: int
    day_min: str
    day_max: str
    hours_count: int
    hour_min: str
    hour_max: str


class AppwidgetsPhoto(PydanticModel):
    id: str
    images: List["BaseImage"]


class AppwidgetsPhotos(PydanticModel):
    count: int
    items: List["AppwidgetsPhoto"]


class AppsApp(PydanticModel):
    allOf: Unsupported


class AppsAppLeaderboardType(enum.IntEnum):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppsAppMin(PydanticModel):
    type: "AppsAppType"
    id: int
    title: str
    author_owner_id: int
    is_installed: bool
    icon_139: str
    icon_150: str
    icon_278: str
    icon_576: str
    background_loader_color: str
    loader_icon: str
    icon_75: str


class AppsAppType(enum.Enum):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class AppsLeaderboard(PydanticModel):
    level: int
    points: int
    score: int
    user_id: int


class AppsScope(PydanticModel):
    name: str
    title: str


class AudioAudio(PydanticModel):
    artist: str
    id: int
    title: str
    url: str
    duration: int
    date: int
    album_id: int
    genre_id: int
    performer: str


class BaseBoolInt(enum.IntEnum):
    NO = 0
    YES = 1


class BaseCity(PydanticModel):
    id: int
    title: str


class BaseCommentsInfo(PydanticModel):
    can_post: "BaseBoolInt"
    count: int
    groups_can_post: bool
    donut: "WallWallpostCommentsDonut"


class BaseCountry(PydanticModel):
    id: int
    title: str


class BaseCropPhoto(PydanticModel):
    photo: "PhotosPhoto"
    crop: "BaseCropPhotoCrop"
    rect: "BaseCropPhotoRect"


class BaseCropPhotoCrop(PydanticModel):
    x: int
    y: int
    x2: int
    y2: int


class BaseCropPhotoRect(PydanticModel):
    x: int
    y: int
    x2: int
    y2: int


class BaseError(PydanticModel):
    error_code: int
    error_subcode: int
    error_msg: str
    error_text: str
    request_params: List["BaseRequestParam"]


class BaseGeo(PydanticModel):
    coordinates: "BaseGeoCoordinates"
    place: "BasePlace"
    showmap: int
    type: str


class BaseGeoCoordinates(PydanticModel):
    latitude: int
    longitude: int


class BaseGradientPoint(PydanticModel):
    color: str
    position: int


class BaseImage(PydanticModel):
    id: str
    height: int
    url: str
    width: int


class BaseLikes(PydanticModel):
    count: int
    user_likes: "BaseBoolInt"


class BaseLikesInfo(PydanticModel):
    can_like: "BaseBoolInt"
    can_publish: "BaseBoolInt"
    count: int
    user_likes: int


class BaseLink(PydanticModel):
    application: "BaseLinkApplication"
    button: "BaseLinkButton"
    caption: str
    description: str
    id: str
    is_favorite: bool
    photo: "PhotosPhoto"
    preview_page: str
    preview_url: str
    product: "BaseLinkProduct"
    rating: "BaseLinkRating"
    title: str
    url: str
    target_object: "LinkTargetObject"
    is_external: bool
    video: "VideoVideo"


class BaseLinkApplication(PydanticModel):
    app_id: int
    store: "BaseLinkApplicationStore"


class BaseLinkApplicationStore(PydanticModel):
    id: int
    name: str


class BaseLinkButton(PydanticModel):
    action: "BaseLinkButtonAction"
    title: str
    block_id: str
    section_id: str
    curator_id: int
    owner_id: int
    icon: str
    style: "BaseLinkButtonStyle"


class BaseLinkButtonAction(PydanticModel):
    type: "BaseLinkButtonActionType"
    url: str
    consume_reason: str


class BaseLinkButtonActionType(enum.Enum):
    OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class BaseLinkProduct(PydanticModel):
    price: "MarketPrice"
    merchant: str
    orders_count: int


class BaseLinkProductStatus(enum.Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class BaseLinkRating(PydanticModel):
    reviews_count: int
    stars: int


class BaseMessageError(PydanticModel):
    code: int
    description: str


class BaseObject(PydanticModel):
    id: int
    title: str


class BaseObjectCount(PydanticModel):
    count: int


class BaseObjectWithName(PydanticModel):
    id: int
    name: str


class BasePlace(PydanticModel):
    address: str
    checkins: int
    city: str
    country: str
    created: int
    icon: str
    id: int
    latitude: int
    longitude: int
    title: str
    type: str


class BasePropertyExists(enum.IntEnum):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(PydanticModel):
    count: int
    wall_count: int
    mail_count: int
    user_reposted: int


class BaseRequestParam(PydanticModel):
    key: str
    value: str


class BaseSex(enum.IntEnum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class BaseSticker(PydanticModel):
    sticker_id: int
    product_id: int
    images: List["BaseImage"]
    images_with_background: List["BaseImage"]
    animation_url: str
    animations: List["BaseStickerAnimation"]
    is_allowed: bool


class BaseStickerAnimation(PydanticModel):
    type: str
    url: str


BaseStickersList = List["BaseSticker"]


class BaseUploadServer(PydanticModel):
    upload_url: str


class BaseUserGroupFields(enum.Enum):
    ABOUT = "about"
    ACTION_BUTTON = "action_button"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    ADMIN_LEVEL = "admin_level"
    AGE_LIMITS = "age_limits"
    AUTHOR_ID = "author_id"
    BAN_INFO = "ban_info"
    BDATE = "bdate"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    BOOKS = "books"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAREER = "career"
    CITY = "city"
    COMMON_COUNT = "common_count"
    CONNECTIONS = "connections"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COUNTRY = "country"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DEACTIVATED = "deactivated"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EDUCATION = "education"
    EXPORTS = "exports"
    FINISH_DATE = "finish_date"
    FIXED_POST = "fixed_post"
    FOLLOWERS_COUNT = "followers_count"
    FRIEND_STATUS = "friend_status"
    GAMES = "games"
    HAS_MARKET_APP = "has_market_app"
    HAS_MOBILE = "has_mobile"
    HAS_PHOTO = "has_photo"
    HOME_TOWN = "home_town"
    ID = "id"
    INTERESTS = "interests"
    IS_ADMIN = "is_admin"
    IS_CLOSED = "is_closed"
    IS_FAVORITE = "is_favorite"
    IS_FRIEND = "is_friend"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MEMBER = "is_member"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    IS_SUBSCRIBED = "is_subscribed"
    LAST_SEEN = "last_seen"
    LINKS = "links"
    LISTS = "lists"
    MAIDEN_NAME = "maiden_name"
    MAIN_ALBUM_ID = "main_album_id"
    MAIN_SECTION = "main_section"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    MEMBERS_COUNT = "members_count"
    MILITARY = "military"
    MOVIES = "movies"
    MUSIC = "music"
    NAME = "name"
    NICKNAME = "nickname"
    OCCUPATION = "occupation"
    ONLINE = "online"
    ONLINE_STATUS = "online_status"
    PERSONAL = "personal"
    PHONE = "phone"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_50 = "photo_50"
    PHOTO_ID = "photo_id"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    QUOTES = "quotes"
    RELATION = "relation"
    RELATIVES = "relatives"
    SCHOOLS = "schools"
    SCREEN_NAME = "screen_name"
    SEX = "sex"
    SITE = "site"
    START_DATE = "start_date"
    STATUS = "status"
    TIMEZONE = "timezone"
    TRENDING = "trending"
    TV = "tv"
    TYPE = "type"
    UNIVERSITIES = "universities"
    VERIFIED = "verified"
    WALL_COMMENTS = "wall_comments"
    WIKI_PAGE = "wiki_page"
    VK_ADMIN_STATUS = "vk_admin_status"


class BaseUserId(PydanticModel):
    user_id: int


class BoardDefaultOrder(enum.IntEnum):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class BoardTopic(PydanticModel):
    comments: int
    created: int
    created_by: int
    id: int
    is_closed: "BaseBoolInt"
    is_fixed: "BaseBoolInt"
    title: str
    updated: int
    updated_by: int


class BoardTopicComment(PydanticModel):
    attachments: List["WallCommentAttachment"]
    date: int
    from_id: int
    id: int
    real_offset: int
    text: str
    can_edit: "BaseBoolInt"
    likes: "BaseLikesInfo"


class BoardTopicPoll(PydanticModel):
    owner_id: int
    poll_id: int
    created: int
    is_closed: "BaseBoolInt"
    question: str
    votes: int
    answer_id: int
    answers: List["PollsAnswer"]


class CallbackBoardPostDelete(PydanticModel):
    topic_owner_id: int
    topic_id: int
    id: int


class CallbackConfirmationMessage(PydanticModel):
    type: "CallbackMessageType"
    group_id: int
    secret: str


class CallbackDonutMoneyWithdraw(PydanticModel):
    amount: int
    amount_without_fee: int


class CallbackDonutMoneyWithdrawError(PydanticModel):
    reason: str


class CallbackDonutSubscriptionCancelled(PydanticModel):
    user_id: int


class CallbackDonutSubscriptionCreate(PydanticModel):
    user_id: int
    amount: int
    amount_without_fee: int


class CallbackDonutSubscriptionExpired(PydanticModel):
    user_id: int


class CallbackDonutSubscriptionPriceChanged(PydanticModel):
    user_id: int
    amount_old: int
    amount_new: int
    amount_diff: int
    amount_diff_without_fee: int


class CallbackDonutSubscriptionProlonged(PydanticModel):
    user_id: int
    amount: int
    amount_without_fee: int


class CallbackGroupChangePhoto(PydanticModel):
    user_id: int
    photo: "PhotosPhoto"


class CallbackGroupChangeSettings(PydanticModel):
    user_id: int
    self: "BaseBoolInt"


class CallbackGroupJoin(PydanticModel):
    user_id: int
    join_type: "CallbackGroupJoinType"


class CallbackGroupJoinType(enum.Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(PydanticModel):
    user_id: int
    self: "BaseBoolInt"


class CallbackGroupMarket(enum.IntEnum):
    DISABLED = 0
    OPEN = 1


class CallbackGroupOfficerRole(enum.IntEnum):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(PydanticModel):
    admin_id: int
    user_id: int
    level_old: "CallbackGroupOfficerRole"
    level_new: "CallbackGroupOfficerRole"


class CallbackGroupSettingsChanges(PydanticModel):
    title: str
    description: str
    access: "GroupsGroupIsClosed"
    screen_name: str
    public_category: int
    public_subcategory: int
    age_limits: "GroupsGroupFullAgeLimits"
    website: str
    enable_status_default: "GroupsGroupWall"
    enable_audio: "GroupsGroupAudio"
    enable_video: "GroupsGroupVideo"
    enable_photo: "GroupsGroupPhotos"
    enable_market: "CallbackGroupMarket"


class CallbackLikeAddRemove(PydanticModel):
    liker_id: int
    object_type: str
    object_owner_id: int
    object_id: int
    post_id: int
    thread_reply_id: int


class CallbackMarketComment(PydanticModel):
    id: int
    from_id: int
    date: int
    text: str
    market_owner_od: int
    photo_id: int


class CallbackMarketCommentDelete(PydanticModel):
    owner_id: int
    id: int
    user_id: int
    item_id: int


class CallbackMessageAllow(PydanticModel):
    user_id: int
    key: str


class CallbackMessageBase(PydanticModel):
    type: "CallbackMessageType"
    object: object
    group_id: int


class CallbackMessageDeny(PydanticModel):
    user_id: int


class CallbackMessageType(enum.Enum):
    AUDIO_NEW = "audio_new"
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"
    CONFIRMATION = "confirmation"
    GROUP_LEAVE = "group_leave"
    GROUP_JOIN = "group_join"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_NEW = "message_new"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_POST_NEW = "wall_post_new"
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"


class CallbackPhotoComment(PydanticModel):
    id: int
    from_id: int
    date: int
    text: str
    photo_owner_od: int


class CallbackPhotoCommentDelete(PydanticModel):
    id: int
    owner_id: int
    user_id: int
    photo_id: int


class CallbackPollVoteNew(PydanticModel):
    owner_id: int
    poll_id: int
    option_id: int
    user_id: int


class CallbackQrScan(PydanticModel):
    user_id: int
    data: str
    type: str
    subtype: str
    reread: bool


class CallbackUserBlock(PydanticModel):
    admin_id: int
    user_id: int
    unblock_date: int
    reason: int
    comment: str


class CallbackUserUnblock(PydanticModel):
    admin_id: int
    user_id: int
    by_end_date: int


class CallbackVideoComment(PydanticModel):
    id: int
    from_id: int
    date: int
    text: str
    video_owner_od: int


class CallbackVideoCommentDelete(PydanticModel):
    id: int
    owner_id: int
    user_id: int
    video_id: int


class CallbackWallCommentDelete(PydanticModel):
    owner_id: int
    id: int
    user_id: int
    post_id: int


class CallsCall(PydanticModel):
    duration: int
    initiator_id: int
    receiver_id: int
    state: "CallsEndState"
    time: int
    video: bool


class CallsEndState(enum.Enum):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class CallsParticipants(PydanticModel):
    list: List[int]
    count: int


class CommentThread(PydanticModel):
    can_post: bool
    count: int
    groups_can_post: bool
    items: List["WallWallComment"]
    show_reply_button: bool


class DatabaseCity(PydanticModel):
    allOf: Unsupported


class DatabaseFaculty(PydanticModel):
    id: int
    title: str


class DatabaseRegion(PydanticModel):
    id: int
    title: str


class DatabaseSchool(PydanticModel):
    id: int
    title: str


class DatabaseStation(PydanticModel):
    city_id: int
    color: str
    id: int
    name: str


class DatabaseUniversity(PydanticModel):
    id: int
    title: str


class DocsDoc(PydanticModel):
    id: int
    owner_id: int
    title: str
    size: int
    ext: str
    url: str
    date: int
    type: int
    preview: "DocsDocPreview"
    is_licensed: "BaseBoolInt"
    access_key: str
    tags: List[str]


class DocsDocAttachmentType(enum.Enum):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(PydanticModel):
    audio_msg: "DocsDocPreviewAudioMsg"
    graffiti: "DocsDocPreviewGraffiti"
    photo: "DocsDocPreviewPhoto"
    video: "DocsDocPreviewVideo"


class DocsDocPreviewAudioMsg(PydanticModel):
    duration: int
    link_mp3: str
    link_ogg: str
    waveform: List[int]


class DocsDocPreviewGraffiti(PydanticModel):
    src: str
    width: int
    height: int


class DocsDocPreviewPhoto(PydanticModel):
    sizes: List["DocsDocPreviewPhotoSizes"]


class DocsDocPreviewPhotoSizes(PydanticModel):
    src: str
    width: int
    height: int
    type: "PhotosPhotoSizesType"


class DocsDocPreviewVideo(PydanticModel):
    src: str
    width: int
    height: int
    file_size: int


class DocsDocTypes(PydanticModel):
    id: int
    name: str
    count: int


class DocsDocUploadResponse(PydanticModel):
    file: str


class DonutDonatorSubscriptionInfo(PydanticModel):
    owner_id: int
    next_payment_date: int
    amount: int
    status: str


class EventsEventAttach(PydanticModel):
    address: str
    button_text: str
    friends: List[int]
    id: int
    is_favorite: bool
    member_status: "GroupsGroupFullMemberStatus"
    text: str
    time: int


class FaveBookmark(PydanticModel):
    added_date: int
    link: "BaseLink"
    post: "WallWallpostFull"
    product: "MarketMarketItem"
    seen: bool
    tags: List["FaveTag"]
    type: "FaveBookmarkType"
    video: "VideoVideo"


class FaveBookmarkType(enum.Enum):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class FavePage(PydanticModel):
    description: str
    group: "GroupsGroupFull"
    tags: List["FaveTag"]
    type: "FavePageType"
    updated_date: int
    user: "UsersUserFull"


class FavePageType(enum.Enum):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(PydanticModel):
    id: int
    name: str


class FriendsFriendExtendedStatus(PydanticModel):
    allOf: Unsupported


class FriendsFriendStatus(PydanticModel):
    friend_status: "FriendsFriendStatusStatus"
    sign: str
    user_id: int


class FriendsFriendStatusStatus(enum.IntEnum):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsFriendsList(PydanticModel):
    id: int
    name: str


class FriendsMutualFriend(PydanticModel):
    common_count: int
    common_friends: List[int]
    id: int


class FriendsRequests(PydanticModel):
    _from: str
    mutual: "FriendsRequestsMutual"
    user_id: int


class FriendsRequestsMutual(PydanticModel):
    count: int
    users: List[int]


class FriendsRequestsXtrMessage(PydanticModel):
    _from: str
    message: str
    mutual: "FriendsRequestsMutual"
    user_id: int


class FriendsUserXtrLists(PydanticModel):
    allOf: Unsupported


class FriendsUserXtrPhone(PydanticModel):
    allOf: Unsupported


class GiftsGift(PydanticModel):
    date: int
    from_id: int
    gift: "GiftsLayout"
    gift_hash: str
    id: int
    message: str
    privacy: "GiftsGiftPrivacy"


class GiftsGiftPrivacy(enum.IntEnum):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(PydanticModel):
    id: int
    thumb_512: str
    thumb_256: str
    thumb_48: str
    thumb_96: str
    stickers_product_id: int
    is_stickers_style: bool
    build_id: str
    keywords: str


class GroupsAddress(PydanticModel):
    additional_address: str
    address: str
    city_id: int
    country_id: int
    distance: int
    id: int
    latitude: int
    longitude: int
    metro_station_id: int
    phone: str
    time_offset: int
    timetable: "GroupsAddressTimetable"
    title: str
    work_info_status: "GroupsAddressWorkInfoStatus"


class GroupsAddressTimetable(PydanticModel):
    fri: "GroupsAddressTimetableDay"
    mon: "GroupsAddressTimetableDay"
    sat: "GroupsAddressTimetableDay"
    sun: "GroupsAddressTimetableDay"
    thu: "GroupsAddressTimetableDay"
    tue: "GroupsAddressTimetableDay"
    wed: "GroupsAddressTimetableDay"


class GroupsAddressTimetableDay(PydanticModel):
    break_close_time: int
    break_open_time: int
    close_time: int
    open_time: int


class GroupsAddressWorkInfoStatus(enum.Enum):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(PydanticModel):
    is_enabled: bool
    main_address_id: int


class GroupsBanInfo(PydanticModel):
    admin_id: int
    comment: str
    comment_visible: bool
    is_closed: bool
    date: int
    end_date: int
    reason: "GroupsBanInfoReason"


class GroupsBanInfoReason(enum.IntEnum):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


GroupsBannedItem = GroupsOwnerXtrBanInfo


class GroupsCallbackServer(PydanticModel):
    id: int
    title: str
    creator_id: int
    url: str
    secret_key: str
    status: str


class GroupsCallbackSettings(PydanticModel):
    api_version: str
    events: "GroupsLongPollEvents"


class GroupsContactsItem(PydanticModel):
    user_id: int
    desc: str
    phone: str
    email: str


class GroupsCountersGroup(PydanticModel):
    addresses: int
    albums: int
    audios: int
    audio_playlists: int
    docs: int
    market: int
    photos: int
    topics: int
    videos: int


class GroupsCover(PydanticModel):
    enabled: "BaseBoolInt"
    images: List["BaseImage"]


class GroupsFields(enum.Enum):
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    REQUESTS_COUNT = "requests_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SUGGEST = "can_suggest"
    CAN_UPLOAD_STORY = "can_upload_story"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_CREATE_TOPIC = "can_create_topic"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    SECONDARY_SECTION = "secondary_section"
    WALL = "wall"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    HAS_GROUP_CHANNEL = "has_group_channel"
    GROUP_CHANNEL = "group_channel"
    ONLINE_STATUS = "online_status"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    ACTION_BUTTON = "action_button"
    AUTHOR_ID = "author_id"
    PHONE = "phone"
    HAS_MARKET_APP = "has_market_app"
    ADDRESSES = "addresses"
    LIVE_COVERS = "live_covers"
    IS_ADULT = "is_adult"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    IS_BUSINESS = "is_business"


class GroupsFilter(enum.Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class GroupsGroup(PydanticModel):
    id: int
    name: str
    screen_name: str
    is_closed: "GroupsGroupIsClosed"
    type: "GroupsGroupType"
    is_admin: "BaseBoolInt"
    admin_level: "GroupsGroupAdminLevel"
    is_member: "BaseBoolInt"
    is_advertiser: "BaseBoolInt"
    start_date: int
    finish_date: int
    deactivated: str
    photo_50: str
    photo_100: str
    photo_200: str


class GroupsGroupAccess(enum.IntEnum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupAdminLevel(enum.IntEnum):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupAgeLimits(enum.IntEnum):
    UNLIMITED = 1
    _16_PLUS = 2
    _18_PLUS = 3


class GroupsGroupAttach(PydanticModel):
    id: int
    text: str
    status: str
    size: int
    is_favorite: bool


class GroupsGroupAudio(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupBanInfo(PydanticModel):
    comment: str
    end_date: int
    reason: "GroupsBanInfoReason"


class GroupsGroupCategory(PydanticModel):
    id: int
    name: str
    subcategories: List["BaseObjectWithName"]


class GroupsGroupCategoryFull(PydanticModel):
    id: int
    name: str
    page_count: int
    page_previews: List["GroupsGroup"]
    subcategories: List["GroupsGroupCategory"]


class GroupsGroupCategoryType(PydanticModel):
    id: int
    name: str


class GroupsGroupDocs(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupFull(PydanticModel):
    allOf: Unsupported


class GroupsGroupFullAgeLimits(enum.IntEnum):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupsGroupFullMainSection(enum.IntEnum):
    ABSENT = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIO = 3
    VIDEO = 4
    MARKET = 5


class GroupsGroupFullMemberStatus(enum.IntEnum):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupsGroupIsClosed(enum.IntEnum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupLink(PydanticModel):
    name: str
    desc: str
    edit_title: "BaseBoolInt"
    id: int
    image_processing: "BaseBoolInt"
    url: str


class GroupsGroupMarketCurrency(enum.IntEnum):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupsGroupPhotos(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupPublicCategoryList(PydanticModel):
    id: int
    name: str
    subcategories: List["GroupsGroupCategoryType"]


class GroupsGroupRole(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupsGroupSubject(enum.Enum):
    1 = "1"
    2 = "2"
    3 = "3"
    4 = "4"
    5 = "5"
    6 = "6"
    7 = "7"
    8 = "8"
    9 = "9"
    10 = "10"
    11 = "11"
    12 = "12"
    13 = "13"
    14 = "14"
    15 = "15"
    16 = "16"
    17 = "17"
    18 = "18"
    19 = "19"
    20 = "20"
    21 = "21"
    22 = "22"
    23 = "23"
    24 = "24"
    25 = "25"
    26 = "26"
    27 = "27"
    28 = "28"
    29 = "29"
    30 = "30"
    31 = "31"
    32 = "32"
    33 = "33"
    34 = "34"
    35 = "35"
    36 = "36"
    37 = "37"
    38 = "38"
    39 = "39"
    40 = "40"
    41 = "41"
    42 = "42"


class GroupsGroupSuggestedPrivacy(enum.IntEnum):
    NONE = 0
    ALL = 1
    SUBSCRIBERS = 2


class GroupsGroupTag(PydanticModel):
    id: int
    name: str
    color: str
    uses: int


class GroupsGroupTopics(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupType(enum.Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupVideo(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupWall(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupsGroupWiki(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupsArray(PydanticModel):
    count: int
    items: List[int]


class GroupsLinksItem(PydanticModel):
    desc: str
    edit_title: "BaseBoolInt"
    id: int
    name: str
    photo_100: str
    photo_50: str
    url: str


class GroupsLiveCovers(PydanticModel):
    is_enabled: bool
    is_scalable: bool
    story_ids: List[str]


class GroupsLongPollEvents(PydanticModel):
    audio_new: "BaseBoolInt"
    board_post_delete: "BaseBoolInt"
    board_post_edit: "BaseBoolInt"
    board_post_new: "BaseBoolInt"
    board_post_restore: "BaseBoolInt"
    group_change_photo: "BaseBoolInt"
    group_change_settings: "BaseBoolInt"
    group_join: "BaseBoolInt"
    group_leave: "BaseBoolInt"
    group_officers_edit: "BaseBoolInt"
    lead_forms_new: "BaseBoolInt"
    market_comment_delete: "BaseBoolInt"
    market_comment_edit: "BaseBoolInt"
    market_comment_new: "BaseBoolInt"
    market_comment_restore: "BaseBoolInt"
    market_order_new: "BaseBoolInt"
    market_order_edit: "BaseBoolInt"
    message_allow: "BaseBoolInt"
    message_deny: "BaseBoolInt"
    message_new: "BaseBoolInt"
    message_read: "BaseBoolInt"
    message_reply: "BaseBoolInt"
    message_typing_state: "BaseBoolInt"
    message_edit: "BaseBoolInt"
    photo_comment_delete: "BaseBoolInt"
    photo_comment_edit: "BaseBoolInt"
    photo_comment_new: "BaseBoolInt"
    photo_comment_restore: "BaseBoolInt"
    photo_new: "BaseBoolInt"
    poll_vote_new: "BaseBoolInt"
    user_block: "BaseBoolInt"
    user_unblock: "BaseBoolInt"
    video_comment_delete: "BaseBoolInt"
    video_comment_edit: "BaseBoolInt"
    video_comment_new: "BaseBoolInt"
    video_comment_restore: "BaseBoolInt"
    video_new: "BaseBoolInt"
    wall_post_new: "BaseBoolInt"
    wall_reply_delete: "BaseBoolInt"
    wall_reply_edit: "BaseBoolInt"
    wall_reply_new: "BaseBoolInt"
    wall_reply_restore: "BaseBoolInt"
    wall_repost: "BaseBoolInt"
    donut_subscription_create: "BaseBoolInt"
    donut_subscription_prolonged: "BaseBoolInt"
    donut_subscription_cancelled: "BaseBoolInt"
    donut_subscription_expired: "BaseBoolInt"
    donut_subscription_price_changed: "BaseBoolInt"
    donut_money_withdraw: "BaseBoolInt"
    donut_money_withdraw_error: "BaseBoolInt"


class GroupsLongPollServer(PydanticModel):
    key: str
    server: str
    ts: str


class GroupsLongPollSettings(PydanticModel):
    api_version: str
    events: "GroupsLongPollEvents"
    is_enabled: bool


class GroupsMarketInfo(PydanticModel):
    contact_id: int
    currency: "MarketCurrency"
    currency_text: str
    enabled: "BaseBoolInt"
    main_album_id: int
    price_max: str
    price_min: str


class GroupsMarketState(enum.Enum):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class GroupsMemberRole(PydanticModel):
    id: int
    permissions: List["GroupsMemberRolePermission"]
    role: "GroupsMemberRoleStatus"


class GroupsMemberRolePermission(enum.Enum):
    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsMemberStatus(PydanticModel):
    member: "BaseBoolInt"
    user_id: int


class GroupsMemberStatusFull(PydanticModel):
    can_invite: "BaseBoolInt"
    can_recall: "BaseBoolInt"
    invitation: "BaseBoolInt"
    member: "BaseBoolInt"
    request: "BaseBoolInt"
    user_id: int


class GroupsOnlineStatus(PydanticModel):
    minutes: int
    status: "GroupsOnlineStatusType"


class GroupsOnlineStatusType(enum.Enum):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(PydanticModel):
    ban_info: "GroupsBanInfo"
    group: "GroupsGroup"
    profile: "UsersUser"
    type: "GroupsOwnerXtrBanInfoType"


class GroupsOwnerXtrBanInfoType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"


class GroupsProfileItem(PydanticModel):
    id: int
    photo_50: str
    photo_100: str
    first_name: str


class GroupsRoleOptions(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsSettingsTwitter(PydanticModel):
    status: str
    name: str


class GroupsSubjectItem(PydanticModel):
    id: int
    name: str


class GroupsTokenPermissionSetting(PydanticModel):
    name: str
    setting: int


class GroupsUserXtrRole(PydanticModel):
    allOf: Unsupported


class LikesType(enum.Enum):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE = "note"
    MARKET = "market"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
    SITEPAGE = "sitepage"


class LinkTargetObject(PydanticModel):
    type: str
    owner_id: int
    item_id: int


class MarketCurrency(PydanticModel):
    id: int
    name: str


class MarketMarketAlbum(PydanticModel):
    count: int
    id: int
    owner_id: int
    photo: "PhotosPhoto"
    title: str
    updated_time: int


MarketMarketCategory = MarketMarketCategoryOld


class MarketMarketCategoryNested(PydanticModel):
    id: int
    name: str
    parent: "MarketMarketCategoryNested"


class MarketMarketCategoryOld(PydanticModel):
    id: int
    name: str
    section: "MarketSection"


class MarketMarketCategoryTree(PydanticModel):
    id: int
    name: str
    children: List["MarketMarketCategoryTree"]


class MarketMarketItem(PydanticModel):
    access_key: str
    availability: "MarketMarketItemAvailability"
    button_title: str
    category: "MarketMarketCategory"
    date: int
    description: str
    external_id: str
    id: int
    is_favorite: bool
    owner_id: int
    price: "MarketPrice"
    thumb_photo: str
    title: str
    url: str
    variants_grouping_id: int
    is_main_variant: bool


class MarketMarketItemAvailability(enum.IntEnum):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketMarketItemFull(PydanticModel):
    allOf: Unsupported


class MarketOrder(PydanticModel):
    id: int
    group_id: int
    user_id: int
    display_order_id: str
    date: int
    status: int
    items_count: int
    track_number: str
    track_link: str
    comment: str
    address: str
    merchant_comment: str
    weight: int
    total_price: "MarketPrice"
    preview_order_items: List["MarketOrderItem"]
    cancel_info: "BaseLink"


class MarketOrderItem(PydanticModel):
    owner_id: int
    item_id: int
    price: "MarketPrice"
    quantity: int
    item: "MarketMarketItem"
    title: str
    photo: "PhotosPhoto"
    variants: List[str]


class MarketPrice(PydanticModel):
    amount: str
    currency: "MarketCurrency"
    discount_rate: int
    old_amount: str
    text: str
    old_amount_text: str


class MarketSection(PydanticModel):
    id: int
    name: str


class MediaRestriction(PydanticModel):
    text: str
    title: str
    button: "VideoRestrictionButton"
    always_shown: "BaseBoolInt"
    blur: "BaseBoolInt"
    can_play: "BaseBoolInt"
    can_preview: "BaseBoolInt"
    card_icon: List["BaseImage"]
    list_icon: List["BaseImage"]


class MessagesAudioMessage(PydanticModel):
    access_key: str
    transcript_error: int
    duration: int
    id: int
    link_mp3: str
    link_ogg: str
    owner_id: int
    waveform: List[int]


class MessagesChat(PydanticModel):
    admin_id: int
    id: int
    kicked: "BaseBoolInt"
    left: "BaseBoolInt"
    photo_100: str
    photo_200: str
    photo_50: str
    push_settings: "MessagesChatPushSettings"
    title: str
    type: str
    users: List[int]
    is_default_photo: bool


class MessagesChatFull(PydanticModel):
    admin_id: int
    id: int
    kicked: "BaseBoolInt"
    left: "BaseBoolInt"
    photo_100: str
    photo_200: str
    photo_50: str
    push_settings: "MessagesChatPushSettings"
    title: str
    type: str
    users: List["MessagesUserXtrInvitedBy"]


class MessagesChatPreview(PydanticModel):
    admin_id: int
    joined: bool
    local_id: int
    members: List[int]
    members_count: int
    title: str
    is_member: bool


class MessagesChatPushSettings(PydanticModel):
    disabled_until: int
    sound: "BaseBoolInt"


class MessagesChatRestrictions(PydanticModel):
    admins_promote_users: bool
    only_admins_edit_info: bool
    only_admins_edit_pin: bool
    only_admins_invite: bool
    only_admins_kick: bool


class MessagesChatSettings(PydanticModel):
    members_count: int
    friends_count: int
    owner_id: int
    title: str
    pinned_message: "MessagesPinnedMessage"
    state: "MessagesChatSettingsState"
    photo: "MessagesChatSettingsPhoto"
    admin_ids: List[int]
    active_ids: List[int]
    is_group_channel: bool
    acl: "MessagesChatSettingsAcl"
    permissions: "MessagesChatSettingsPermissions"
    is_disappearing: bool
    theme: str
    disappearing_chat_link: str
    is_service: bool


class MessagesChatSettingsAcl(PydanticModel):
    can_change_info: bool
    can_change_invite_link: bool
    can_change_pin: bool
    can_invite: bool
    can_promote_users: bool
    can_see_invite_link: bool
    can_moderate: bool
    can_copy_chat: bool
    can_call: bool
    can_use_mass_mentions: bool
    can_change_service_type: bool


class MessagesChatSettingsPermissions(PydanticModel):
    invite: str
    change_info: str
    change_pin: str
    use_mass_mentions: str
    see_invite_link: str
    call: str
    change_admins: str


class MessagesChatSettingsPhoto(PydanticModel):
    photo_50: str
    photo_100: str
    photo_200: str
    is_default_photo: bool


class MessagesChatSettingsState(enum.Enum):
    IN = "in"
    KICKED = "kicked"
    LEFT = "left"


class MessagesConversation(PydanticModel):
    peer: "MessagesConversationPeer"
    sort_id: "MessagesConversationSortId"
    last_message_id: int
    in_read: int
    out_read: int
    unread_count: int
    is_marked_unread: bool
    out_read_by: "MessagesOutReadBy"
    important: bool
    unanswered: bool
    special_service_type: str
    message_request_data: "MessagesMessageRequestData"
    mentions: List[int]
    current_keyboard: "MessagesKeyboard"
    push_settings: "MessagesPushSettings"
    can_write: "MessagesConversationCanWrite"
    chat_settings: "MessagesChatSettings"


class MessagesConversationCanWrite(PydanticModel):
    allowed: bool
    reason: int


class MessagesConversationMember(PydanticModel):
    can_kick: bool
    invited_by: int
    is_admin: bool
    is_owner: bool
    is_message_request: bool
    join_date: int
    request_date: int
    member_id: int


class MessagesConversationPeer(PydanticModel):
    id: int
    local_id: int
    type: "MessagesConversationPeerType"


class MessagesConversationPeerType(enum.Enum):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationSortId(PydanticModel):
    major_id: int
    minor_id: int


class MessagesConversationWithMessage(PydanticModel):
    conversation: "MessagesConversation"
    last_message: "MessagesMessage"


class MessagesForeignMessage(PydanticModel):
    attachments: List["MessagesMessageAttachment"]
    conversation_message_id: int
    date: int
    from_id: int
    fwd_messages: List["MessagesForeignMessage"]
    geo: "BaseGeo"
    id: int
    peer_id: int
    reply_message: "MessagesForeignMessage"
    text: str
    update_time: int
    was_listened: bool
    payload: str


class MessagesForward(PydanticModel):
    owner_id: int
    peer_id: int
    conversation_message_ids: List[int]
    message_ids: List[int]
    is_reply: bool


class MessagesGraffiti(PydanticModel):
    access_key: str
    height: int
    id: int
    owner_id: int
    url: str
    width: int


class MessagesHistoryAttachment(PydanticModel):
    attachment: "MessagesHistoryMessageAttachment"
    message_id: int
    from_id: int
    forward_level: int


class MessagesHistoryMessageAttachment(PydanticModel):
    audio: "AudioAudio"
    audio_message: "MessagesAudioMessage"
    doc: "DocsDoc"
    graffiti: "MessagesGraffiti"
    link: "BaseLink"
    market: "BaseLink"
    photo: "PhotosPhoto"
    share: "BaseLink"
    type: "MessagesHistoryMessageAttachmentType"
    video: "VideoVideo"
    wall: "BaseLink"


class MessagesHistoryMessageAttachmentType(enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(PydanticModel):
    author_id: int
    buttons: List[List["MessagesKeyboardButton"]]
    one_time: bool
    inline: bool


class MessagesKeyboardButton(PydanticModel):
    action: "MessagesKeyboardButtonAction"
    color: str


class MessagesKeyboardButtonAction(PydanticModel):
    app_id: int
    hash: str
    label: str
    link: str
    owner_id: int
    payload: str
    type: "MessagesTemplateActionTypeNames"


class MessagesLastActivity(PydanticModel):
    online: "BaseBoolInt"
    time: int


class MessagesLongpollMessages(PydanticModel):
    count: int
    items: List["MessagesMessage"]


class MessagesLongpollParams(PydanticModel):
    server: str
    key: str
    ts: int
    pts: int


class MessagesMessage(PydanticModel):
    action: "MessagesMessageAction"
    admin_author_id: int
    attachments: List["MessagesMessageAttachment"]
    conversation_message_id: int
    date: int
    deleted: "BaseBoolInt"
    from_id: int
    fwd_messages: List["MessagesForeignMessage"]
    geo: "BaseGeo"
    id: int
    important: bool
    is_hidden: bool
    is_cropped: bool
    keyboard: "MessagesKeyboard"
    members_count: int
    out: "BaseBoolInt"
    payload: str
    peer_id: int
    random_id: int
    ref: str
    ref_source: str
    reply_message: "MessagesForeignMessage"
    text: str
    update_time: int
    was_listened: bool
    pinned_at: int


class MessagesMessageAction(PydanticModel):
    conversation_message_id: int
    email: str
    member_id: int
    message: str
    photo: "MessagesMessageActionPhoto"
    text: str
    type: "MessagesMessageActionStatus"


class MessagesMessageActionPhoto(PydanticModel):
    photo_100: str
    photo_200: str
    photo_50: str


class MessagesMessageActionStatus(enum.Enum):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"


class MessagesMessageAttachment(PydanticModel):
    audio: "AudioAudio"
    audio_message: "MessagesAudioMessage"
    call: "CallsCall"
    doc: "DocsDoc"
    gift: "GiftsLayout"
    graffiti: "MessagesGraffiti"
    link: "BaseLink"
    market: "MarketMarketItem"
    market_market_album: "MarketMarketAlbum"
    photo: "PhotosPhoto"
    sticker: "BaseSticker"
    story: "StoriesStory"
    type: "MessagesMessageAttachmentType"
    video: "VideoVideo"
    wall: "WallWallpostFull"
    wall_reply: "WallWallComment"
    poll: "PollsPoll"


class MessagesMessageAttachmentType(enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    POLL = "poll"
    CALL = "call"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(PydanticModel):
    status: str
    inviter_id: int
    request_date: int


class MessagesMessagesArray(PydanticModel):
    count: int
    items: List["MessagesMessage"]


class MessagesOutReadBy(PydanticModel):
    count: int
    member_ids: List[int]


class MessagesPinnedMessage(PydanticModel):
    attachments: List["MessagesMessageAttachment"]
    conversation_message_id: int
    date: int
    from_id: int
    fwd_messages: List["MessagesForeignMessage"]
    geo: "BaseGeo"
    id: int
    peer_id: int
    reply_message: "MessagesForeignMessage"
    text: str
    keyboard: "MessagesKeyboard"


class MessagesPushSettings(PydanticModel):
    disabled_forever: bool
    disabled_until: int
    no_sound: bool


class MessagesTemplateActionTypeNames(enum.Enum):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CALLBACK = "callback"


class MessagesUserXtrInvitedBy(PydanticModel):
    allOf: Unsupported


class NewsfeedCommentsFilters(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedEventActivity(PydanticModel):
    address: str
    button_text: str
    friends: List[int]
    member_status: "GroupsGroupFullMemberStatus"
    text: str
    time: int


class NewsfeedFilters(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    RECOMMENDED_GROUPS = "recommended_groups"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    AUDIO_PLAYLIST = "audio_playlist"
    GAMES_CAROUSEL = "games_carousel"
    CLIP = "clip"
    RECOMMENDED_GAME = "recommended_game"


class NewsfeedIgnoreItemType(enum.Enum):
    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemAudio(PydanticModel):
    allOf: Unsupported


class NewsfeedItemAudioAudio(PydanticModel):
    count: int
    items: List["AudioAudio"]


class NewsfeedItemBase(PydanticModel):
    type: "NewsfeedNewsfeedItemType"
    source_id: int
    date: int


class NewsfeedItemDigest(PydanticModel):
    allOf: Unsupported


class NewsfeedItemDigestButton(PydanticModel):
    title: str
    style: str


class NewsfeedItemDigestFooter(PydanticModel):
    style: str
    text: str
    button: "NewsfeedItemDigestButton"


class NewsfeedItemDigestFullItem(PydanticModel):
    text: str
    source_name: str
    attachment_index: int
    attachment: "WallWallpostAttachment"
    style: str
    post: "WallWallpost"


class NewsfeedItemDigestHeader(PydanticModel):
    title: str
    subtitle: str
    style: str
    button: "NewsfeedItemDigestButton"


NewsfeedItemDigestItem = WallWallpost


class NewsfeedItemFriend(PydanticModel):
    allOf: Unsupported


class NewsfeedItemFriendFriends(PydanticModel):
    count: int
    items: List["BaseUserId"]


class NewsfeedItemHolidayRecommendationsBlockHeader(PydanticModel):
    title: str
    subtitle: str
    image: List["BaseImage"]
    action: "BaseLinkButtonAction"


class NewsfeedItemPhoto(PydanticModel):
    allOf: Unsupported


class NewsfeedItemPhotoPhotos(PydanticModel):
    count: int
    items: List["NewsfeedNewsfeedPhoto"]


class NewsfeedItemPhotoTag(PydanticModel):
    allOf: Unsupported


class NewsfeedItemPhotoTagPhotoTags(PydanticModel):
    count: int
    items: List["NewsfeedNewsfeedPhoto"]


class NewsfeedItemPromoButton(PydanticModel):
    allOf: Unsupported


class NewsfeedItemPromoButtonAction(PydanticModel):
    url: str
    type: str
    target: str


class NewsfeedItemPromoButtonImage(PydanticModel):
    width: int
    height: int
    url: str


class NewsfeedItemTopic(PydanticModel):
    allOf: Unsupported


class NewsfeedItemVideo(PydanticModel):
    allOf: Unsupported


class NewsfeedItemVideoVideo(PydanticModel):
    count: int
    items: List["VideoVideo"]


class NewsfeedItemWallpost(PydanticModel):
    allOf: Unsupported


class NewsfeedItemWallpostFeedback(PydanticModel):
    type: "NewsfeedItemWallpostFeedbackType"
    question: str
    answers: List["NewsfeedItemWallpostFeedbackAnswer"]
    stars_count: int
    gratitude: str


class NewsfeedItemWallpostFeedbackAnswer(PydanticModel):
    title: str
    id: str


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedItemWallpostType(enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"


class NewsfeedList(PydanticModel):
    id: int
    title: str


class NewsfeedListFull(PydanticModel):
    allOf: Unsupported


class NewsfeedNewsfeedItem(PydanticModel):
    allOf: Unsupported


class NewsfeedNewsfeedItemType(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"


class NewsfeedNewsfeedPhoto(PydanticModel):
    allOf: Unsupported


class NotesNote(PydanticModel):
    read_comments: int
    can_comment: "BaseBoolInt"
    comments: int
    date: int
    id: int
    owner_id: int
    text: str
    text_wiki: str
    title: str
    view_url: str


class NotesNoteComment(PydanticModel):
    date: int
    id: int
    message: str
    nid: int
    oid: int
    reply_to: int
    uid: int


class NotificationsFeedback(PydanticModel):
    attachments: List["WallWallpostAttachment"]
    from_id: int
    geo: "BaseGeo"
    id: int
    likes: "BaseLikesInfo"
    text: str
    to_id: int


class NotificationsNotification(PydanticModel):
    date: int
    feedback: "NotificationsFeedback"
    parent: "NotificationsNotificationParent"
    reply: "NotificationsReply"
    type: str


class NotificationsNotificationItem(PydanticModel):
    allOf: Unsupported


class NotificationsNotificationParent(PydanticModel):
    allOf: Unsupported


class NotificationsNotificationsComment(PydanticModel):
    date: int
    id: int
    owner_id: int
    photo: "PhotosPhoto"
    post: "WallWallpost"
    text: str
    topic: "BoardTopic"
    video: "VideoVideo"


class NotificationsReply(PydanticModel):
    date: int
    id: int
    text: int


class NotificationsSendMessageError(PydanticModel):
    code: int
    description: str


class NotificationsSendMessageItem(PydanticModel):
    user_id: int
    status: bool
    error: "NotificationsSendMessageError"


class OauthError(PydanticModel):
    error: str
    error_description: str
    redirect_uri: str


class OrdersAmount(PydanticModel):
    amounts: List["OrdersAmountItem"]
    currency: str


class OrdersAmountItem(PydanticModel):
    amount: int
    description: str
    votes: str


class OrdersOrder(PydanticModel):
    amount: int
    app_order_id: int
    cancel_transaction_id: int
    date: int
    id: int
    item: str
    receiver_id: int
    status: str
    transaction_id: int
    user_id: int


class OrdersSubscription(PydanticModel):
    cancel_reason: str
    create_time: int
    id: int
    item_id: str
    next_bill_time: int
    pending_cancel: bool
    period: int
    period_start_time: int
    price: int
    status: str
    test_mode: bool
    trial_expire_time: int
    update_time: int


class OwnerState(PydanticModel):
    state: int
    description: str


class PagesPrivacySettings(enum.IntEnum):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class PagesWikipage(PydanticModel):
    creator_id: int
    creator_name: int
    editor_id: int
    editor_name: str
    group_id: int
    id: int
    title: str
    views: int
    who_can_edit: "PagesPrivacySettings"
    who_can_view: "PagesPrivacySettings"


class PagesWikipageFull(PydanticModel):
    created: int
    creator_id: int
    current_user_can_edit: "BaseBoolInt"
    current_user_can_edit_access: "BaseBoolInt"
    edited: int
    editor_id: int
    group_id: int
    html: str
    id: int
    source: str
    title: str
    view_url: str
    views: int
    who_can_edit: "PagesPrivacySettings"
    who_can_view: "PagesPrivacySettings"


class PagesWikipageHistory(PydanticModel):
    id: int
    length: int
    date: int
    editor_id: int
    editor_name: str


class PhotosCommentXtrPid(PydanticModel):
    attachments: List["WallCommentAttachment"]
    date: int
    from_id: int
    id: int
    likes: "BaseLikesInfo"
    pid: int
    reply_to_comment: int
    reply_to_user: int
    text: str
    parents_stack: List[int]
    thread: "CommentThread"


class PhotosImage(PydanticModel):
    height: int
    type: "PhotosImageType"
    url: str
    width: int


class PhotosImageType(enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"


class PhotosMarketAlbumUploadResponse(PydanticModel):
    gid: int
    hash: str
    photo: str
    server: int


class PhotosMarketUploadResponse(PydanticModel):
    crop_data: str
    crop_hash: str
    group_id: int
    hash: str
    photo: str
    server: int


class PhotosMessageUploadResponse(PydanticModel):
    hash: str
    photo: str
    server: int


class PhotosOwnerUploadResponse(PydanticModel):
    hash: str
    photo: str
    server: int


class PhotosPhoto(PydanticModel):
    access_key: str
    album_id: int
    date: int
    height: int
    id: int
    images: List["PhotosImage"]
    lat: int
    long: int
    owner_id: int
    photo_256: str
    can_comment: "BaseBoolInt"
    place: str
    post_id: int
    sizes: List["PhotosPhotoSizes"]
    text: str
    user_id: int
    width: int
    has_tags: bool
    restrictions: "MediaRestriction"


class PhotosPhotoAlbum(PydanticModel):
    created: int
    description: str
    id: int
    owner_id: int
    size: int
    thumb: "PhotosPhoto"
    title: str
    updated: int


class PhotosPhotoAlbumFull(PydanticModel):
    can_upload: "BaseBoolInt"
    comments_disabled: "BaseBoolInt"
    created: int
    description: str
    id: int
    owner_id: int
    size: int
    sizes: List["PhotosPhotoSizes"]
    thumb_id: int
    thumb_is_last: "BaseBoolInt"
    thumb_src: str
    title: str
    updated: int
    upload_by_admins_only: "BaseBoolInt"


class PhotosPhotoFalseable(PydanticModel):
    allOf: Unsupported


class PhotosPhotoFull(PydanticModel):
    access_key: str
    album_id: int
    can_comment: "BaseBoolInt"
    date: int
    height: int
    id: int
    images: List["PhotosImage"]
    lat: int
    likes: "BaseLikes"
    reposts: "BaseRepostsInfo"
    comments: "BaseObjectCount"
    long: int
    owner_id: int
    post_id: int
    tags: "BaseObjectCount"
    text: str
    user_id: int
    width: int


class PhotosPhotoFullXtrRealOffset(PydanticModel):
    access_key: str
    album_id: int
    can_comment: "BaseBoolInt"
    comments: "BaseObjectCount"
    date: int
    height: int
    hidden: "BasePropertyExists"
    id: int
    lat: int
    likes: "BaseLikes"
    long: int
    owner_id: int
    photo_1280: str
    photo_130: str
    photo_2560: str
    photo_604: str
    photo_75: str
    photo_807: str
    post_id: int
    real_offset: int
    reposts: "BaseObjectCount"
    sizes: List["PhotosPhotoSizes"]
    tags: "BaseObjectCount"
    text: str
    user_id: int
    width: int


class PhotosPhotoSizes(PydanticModel):
    height: int
    url: str
    src: str
    type: "PhotosPhotoSizesType"
    width: int


class PhotosPhotoSizesType(enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"
    A = "a"
    B = "b"
    E = "e"
    I = "i"
    D = "d"
    J = "j"
    TEMP = "temp"
    H = "h"
    G = "g"
    N = "n"
    F = "f"
    MAX = "max"


class PhotosPhotoTag(PydanticModel):
    date: int
    id: int
    placer_id: int
    tagged_name: str
    description: str
    user_id: int
    viewed: "BaseBoolInt"
    x: int
    x2: int
    y: int
    y2: int


class PhotosPhotoUpload(PydanticModel):
    album_id: int
    upload_url: str
    fallback_upload_url: str
    user_id: int
    group_id: int


class PhotosPhotoUploadResponse(PydanticModel):
    aid: int
    hash: str
    photo: str
    photos_list: str
    server: int


class PhotosPhotoXtrRealOffset(PydanticModel):
    access_key: str
    album_id: int
    date: int
    height: int
    hidden: "BasePropertyExists"
    id: int
    lat: int
    long: int
    owner_id: int
    photo_1280: str
    photo_130: str
    photo_2560: str
    photo_604: str
    photo_75: str
    photo_807: str
    post_id: int
    real_offset: int
    sizes: List["PhotosPhotoSizes"]
    text: str
    user_id: int
    width: int


class PhotosPhotoXtrTagInfo(PydanticModel):
    access_key: str
    album_id: int
    date: int
    height: int
    id: int
    lat: int
    long: int
    owner_id: int
    photo_1280: str
    photo_130: str
    photo_2560: str
    photo_604: str
    photo_75: str
    photo_807: str
    placer_id: int
    post_id: int
    sizes: List["PhotosPhotoSizes"]
    tag_created: int
    tag_id: int
    text: str
    user_id: int
    width: int


class PhotosTagsSuggestionItem(PydanticModel):
    title: str
    caption: str
    type: str
    buttons: List["PhotosTagsSuggestionItemButton"]
    photo: "PhotosPhoto"
    tags: List["PhotosPhotoTag"]
    track_code: str


class PhotosTagsSuggestionItemButton(PydanticModel):
    title: str
    action: str
    style: str


class PhotosWallUploadResponse(PydanticModel):
    hash: str
    photo: str
    server: int


class PollsAnswer(PydanticModel):
    id: int
    rate: int
    text: str
    votes: int


class PollsBackground(PydanticModel):
    angle: int
    color: str
    height: int
    id: int
    name: str
    images: List["BaseImage"]
    points: List["BaseGradientPoint"]
    type: str
    width: int


class PollsFriend(PydanticModel):
    id: int


class PollsPoll(PydanticModel):
    anonymous: "PollsPollAnonymous"
    friends: List["PollsFriend"]
    multiple: bool
    answer_id: int
    end_date: int
    answer_ids: List[int]
    closed: bool
    is_board: bool
    can_edit: bool
    can_vote: bool
    can_report: bool
    can_share: bool
    photo: "PollsBackground"
    answers: List["PollsAnswer"]
    created: int
    id: int
    owner_id: int
    author_id: int
    question: str
    background: "PollsBackground"
    votes: int
    disable_unvote: bool


PollsPollAnonymous = bool


class PollsVoters(PydanticModel):
    answer_id: int
    users: "PollsVotersUsers"


class PollsVotersUsers(PydanticModel):
    count: int
    items: List[int]


class PrettycardsPrettycard(PydanticModel):
    button: str
    button_text: str
    card_id: str
    images: List["BaseImage"]
    link_url: str
    photo: str
    price: str
    price_old: str
    title: str


class SearchHint(PydanticModel):
    app: "AppsApp"
    description: str
    _global: "BaseBoolInt"
    group: "GroupsGroup"
    profile: "UsersUserMin"
    section: "SearchHintSection"
    type: "SearchHintType"


class SearchHintSection(enum.Enum):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"


class SearchHintType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"


class SecureLevel(PydanticModel):
    level: int
    uid: int


class SecureSmsNotification(PydanticModel):
    app_id: str
    date: str
    id: str
    message: str
    user_id: str


class SecureTokenChecked(PydanticModel):
    date: int
    expire: int
    success: int
    user_id: int


class SecureTransaction(PydanticModel):
    date: int
    id: int
    uid_from: int
    uid_to: int
    votes: int


class StatsActivity(PydanticModel):
    comments: int
    copies: int
    hidden: int
    likes: int
    subscribed: int
    unsubscribed: int


class StatsCity(PydanticModel):
    count: int
    name: str
    value: int


class StatsCountry(PydanticModel):
    code: str
    count: int
    name: str
    value: int


class StatsPeriod(PydanticModel):
    activity: "StatsActivity"
    period_from: int
    period_to: int
    reach: "StatsReach"
    visitors: "StatsViews"


class StatsReach(PydanticModel):
    age: List["StatsSexAge"]
    cities: List["StatsCity"]
    countries: List["StatsCountry"]
    mobile_reach: int
    reach: int
    reach_subscribers: int
    sex: List["StatsSexAge"]
    sex_age: List["StatsSexAge"]


class StatsSexAge(PydanticModel):
    count: int
    value: str
    reach: int
    reach_subscribers: int
    count_subscribers: int


class StatsViews(PydanticModel):
    age: List["StatsSexAge"]
    cities: List["StatsCity"]
    countries: List["StatsCountry"]
    mobile_views: int
    sex: List["StatsSexAge"]
    sex_age: List["StatsSexAge"]
    views: int
    visitors: int


class StatsWallpostStat(PydanticModel):
    post_id: int
    hide: int
    join_group: int
    links: int
    reach_subscribers: int
    reach_subscribers_count: int
    reach_total: int
    reach_total_count: int
    reach_viral: int
    reach_ads: int
    report: int
    to_group: int
    unsubscribe: int
    sex_age: List["StatsSexAge"]


class StatusStatus(PydanticModel):
    text: str
    audio: "AudioAudio"


class StorageValue(PydanticModel):
    key: str
    value: str


class StoreProduct(PydanticModel):
    id: int
    type: str
    purchased: "BaseBoolInt"
    active: "BaseBoolInt"
    promoted: "BaseBoolInt"
    purchase_date: int
    title: str
    stickers: "BaseStickersList"
    icon: "StoreProductIcon"
    previews: List["BaseImage"]
    has_animation: bool
    subtitle: str


StoreProductIcon = List["BaseImage"]


class StoreStickersKeyword(PydanticModel):
    words: List[str]
    user_stickers: "StoreStickersKeywordStickers"
    promoted_stickers: "StoreStickersKeywordStickers"
    stickers: List["StoreStickersKeywordSticker"]


class StoreStickersKeywordSticker(PydanticModel):
    pack_id: int
    sticker_id: int


StoreStickersKeywordStickers = BaseStickersList


class StoriesClickableArea(PydanticModel):
    x: int
    y: int


class StoriesClickableSticker(PydanticModel):
    clickable_area: List["StoriesClickableArea"]
    id: int
    hashtag: str
    link_object: "BaseLink"
    mention: str
    tooltip_text: str
    owner_id: int
    story_id: int
    question: str
    question_button: str
    place_id: int
    market_item: "MarketMarketItem"
    audio: "AudioAudio"
    audio_start_time: int
    style: str
    type: str
    subtype: str
    post_owner_id: int
    post_id: int
    poll: "PollsPoll"
    color: str
    sticker_id: int
    sticker_pack_id: int
    app: "AppsAppMin"
    app_context: str
    has_new_interactions: bool
    is_broadcast_notify_allowed: bool
    situational_theme_id: int
    situational_app_url: str


class StoriesClickableStickers(PydanticModel):
    clickable_stickers: List["StoriesClickableSticker"]
    original_height: int
    original_width: int


class StoriesFeedItem(PydanticModel):
    type: str
    id: str
    stories: List["StoriesStory"]
    grouped: List["StoriesFeedItem"]
    app: "AppsAppMin"
    promo_data: "StoriesPromoBlock"
    birthday_user_id: int


class StoriesPromoBlock(PydanticModel):
    name: str
    photo_50: str
    photo_100: str
    not_animated: bool


class StoriesReplies(PydanticModel):
    count: int
    new: int


class StoriesStatLine(PydanticModel):
    name: str
    counter: int
    is_unavailable: bool


class StoriesStory(PydanticModel):
    access_key: str
    can_comment: "BaseBoolInt"
    can_reply: "BaseBoolInt"
    can_see: "BaseBoolInt"
    can_like: bool
    can_share: "BaseBoolInt"
    can_hide: "BaseBoolInt"
    date: int
    expires_at: int
    id: int
    is_deleted: bool
    is_expired: bool
    link: "StoriesStoryLink"
    owner_id: int
    parent_story: "StoriesStory"
    parent_story_access_key: str
    parent_story_id: int
    parent_story_owner_id: int
    photo: "PhotosPhoto"
    replies: "StoriesReplies"
    seen: "BaseBoolInt"
    type: "StoriesStoryType"
    clickable_stickers: "StoriesClickableStickers"
    video: "VideoVideo"
    views: int
    can_ask: "BaseBoolInt"
    can_ask_anonymous: "BaseBoolInt"
    narratives_count: int
    first_narrative_title: str
    birthday_wish_user_id: int
    can_use_in_narrative: bool


class StoriesStoryLink(PydanticModel):
    text: str
    url: str


class StoriesStoryStats(PydanticModel):
    answer: "StoriesStoryStatsStat"
    bans: "StoriesStoryStatsStat"
    open_link: "StoriesStoryStatsStat"
    replies: "StoriesStoryStatsStat"
    shares: "StoriesStoryStatsStat"
    subscribers: "StoriesStoryStatsStat"
    views: "StoriesStoryStatsStat"
    likes: "StoriesStoryStatsStat"


class StoriesStoryStatsStat(PydanticModel):
    count: int
    state: "StoriesStoryStatsState"


class StoriesStoryStatsState(enum.Enum):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoriesStoryType(enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    BIRTHDAY_INVITE = "birthday_invite"


class StoriesUploadLinkText(enum.Enum):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"


class StoriesViewersItem(PydanticModel):
    is_liked: bool
    user_id: int
    user: "UsersUserFull"


class UsersCareer(PydanticModel):
    city_id: int
    city_name: str
    company: str
    country_id: int
    _from: int
    group_id: int
    id: int
    position: str
    until: int


class UsersExports(PydanticModel):
    facebook: int
    livejournal: int
    twitter: int


class UsersFields(enum.Enum):
    FIRST_NAME_NOM = "first_name_nom"
    FIRST_NAME_GEN = "first_name_gen"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_INS = "first_name_ins"
    FIRST_NAME_ABL = "first_name_abl"
    LAST_NAME_NOM = "last_name_nom"
    LAST_NAME_GEN = "last_name_gen"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_INS = "last_name_ins"
    LAST_NAME_ABL = "last_name_abl"
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_MAX_SIZE = "photo_max_size"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    ACTIVITIES = "activities"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    SERVICE_DESCRIPTION = "service_description"
    IS_DEAD = "is_dead"


class UsersLastSeen(PydanticModel):
    platform: int
    time: int


class UsersMilitary(PydanticModel):
    country_id: int
    _from: int
    id: int
    unit: str
    unit_id: int
    until: int


class UsersOccupation(PydanticModel):
    id: int
    name: str
    type: str


class UsersOnlineInfo(PydanticModel):
    visible: bool
    last_seen: int
    is_online: bool
    app_id: int
    is_mobile: bool
    status: str


class UsersPersonal(PydanticModel):
    alcohol: int
    inspired_by: str
    langs: List[str]
    life_main: int
    people_main: int
    political: int
    religion: str
    religion_id: int
    smoking: int


class UsersRelative(PydanticModel):
    birth_date: str
    id: int
    name: str
    type: str


class UsersSchool(PydanticModel):
    city: int
    _class: str
    country: int
    id: str
    name: str
    type: int
    type_str: str
    year_from: int
    year_graduated: int
    year_to: int
    speciality: str


class UsersSubscriptionsItem(PydanticModel):
    allOf: Unsupported


class UsersUniversity(PydanticModel):
    chair: int
    chair_name: str
    city: int
    country: int
    education_form: str
    education_status: str
    faculty: int
    faculty_name: str
    graduation: int
    id: int
    name: str
    university_group_id: int


class UsersUser(PydanticModel):
    allOf: Unsupported


class UsersUserConnections(PydanticModel):
    skype: str
    facebook: str
    facebook_name: str
    twitter: str
    livejournal: str
    instagram: str


class UsersUserCounters(PydanticModel):
    albums: int
    audios: int
    followers: int
    friends: int
    gifts: int
    groups: int
    notes: int
    online_friends: int
    pages: int
    photos: int
    subscriptions: int
    user_photos: int
    user_videos: int
    videos: int
    new_photo_tags: int
    new_recognition_tags: int
    mutual_friends: int
    posts: int
    articles: int
    wishes: int
    podcasts: int
    clips: int
    clips_followers: int


class UsersUserFull(PydanticModel):
    allOf: Unsupported


class UsersUserMin(PydanticModel):
    deactivated: str
    first_name: str
    hidden: int
    id: int
    last_name: str
    can_access_closed: bool
    is_closed: bool


class UsersUserRelation(enum.IntEnum):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8


class UsersUserSettingsXtr(PydanticModel):
    connections: "UsersUserConnections"
    bdate: str
    bdate_visibility: int
    city: "BaseCity"
    country: "BaseCountry"
    first_name: str
    home_town: str
    last_name: str
    maiden_name: str
    name_request: "AccountNameRequest"
    personal: "UsersPersonal"
    phone: str
    relation: "UsersUserRelation"
    relation_partner: "UsersUserMin"
    relation_pending: "BaseBoolInt"
    relation_requests: List["UsersUserMin"]
    screen_name: str
    sex: "BaseSex"
    status: str
    status_audio: "AudioAudio"
    interests: "AccountUserSettingsInterests"
    languages: List[str]


class UsersUserType(enum.Enum):
    PROFILE = "profile"


class UsersUserXtrCounters(PydanticModel):
    allOf: Unsupported


class UsersUserXtrType(PydanticModel):
    allOf: Unsupported


class UsersUsersArray(PydanticModel):
    count: int
    items: List[int]


class UtilsDomainResolved(PydanticModel):
    object_id: int
    group_id: int
    type: "UtilsDomainResolvedType"


class UtilsDomainResolvedType(enum.Enum):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(PydanticModel):
    access_key: str
    key: str
    short_url: str
    timestamp: int
    url: str
    views: int


class UtilsLinkChecked(PydanticModel):
    link: str
    status: "UtilsLinkCheckedStatus"


class UtilsLinkCheckedStatus(enum.Enum):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(PydanticModel):
    key: str
    stats: List["UtilsStats"]


class UtilsLinkStatsExtended(PydanticModel):
    key: str
    stats: List["UtilsStatsExtended"]


class UtilsShortLink(PydanticModel):
    access_key: str
    key: str
    short_url: str
    url: str


class UtilsStats(PydanticModel):
    timestamp: int
    views: int


class UtilsStatsCity(PydanticModel):
    city_id: int
    views: int


class UtilsStatsCountry(PydanticModel):
    country_id: int
    views: int


class UtilsStatsExtended(PydanticModel):
    cities: List["UtilsStatsCity"]
    countries: List["UtilsStatsCountry"]
    sex_age: List["UtilsStatsSexAge"]
    timestamp: int
    views: int


class UtilsStatsSexAge(PydanticModel):
    age_range: str
    female: int
    male: int


class VideoLiveInfo(PydanticModel):
    enabled: "BaseBoolInt"
    is_notifications_blocked: "BaseBoolInt"


class VideoLiveSettings(PydanticModel):
    can_rewind: "BaseBoolInt"
    is_endless: "BaseBoolInt"
    max_duration: int


class VideoRestrictionButton(PydanticModel):
    action: str
    title: str


class VideoSaveResult(PydanticModel):
    access_key: str
    description: str
    owner_id: int
    title: str
    upload_url: str
    video_id: int


class VideoVideo(PydanticModel):
    allOf: Unsupported


class VideoVideoAlbumFull(PydanticModel):
    count: int
    id: int
    image: List["VideoVideoImage"]
    image_blur: "BasePropertyExists"
    is_system: "BasePropertyExists"
    owner_id: int
    title: str
    updated_time: int


class VideoVideoFiles(PydanticModel):
    external: str
    mp4_240: str
    mp4_360: str
    mp4_480: str
    mp4_720: str
    mp4_1080: str
    flv_320: str


class VideoVideoFull(PydanticModel):
    allOf: Unsupported


class VideoVideoImage(PydanticModel):
    allOf: Unsupported


class WallAppPost(PydanticModel):
    id: int
    name: str
    photo_130: str
    photo_604: str


class WallAttachedNote(PydanticModel):
    comments: int
    date: int
    id: int
    owner_id: int
    read_comments: int
    title: str
    view_url: str


class WallCarouselBase(PydanticModel):
    carousel_offset: int


class WallCommentAttachment(PydanticModel):
    audio: "AudioAudio"
    doc: "DocsDoc"
    link: "BaseLink"
    market: "MarketMarketItem"
    market_market_album: "MarketMarketAlbum"
    note: "WallAttachedNote"
    page: "PagesWikipageFull"
    photo: "PhotosPhoto"
    sticker: "BaseSticker"
    type: "WallCommentAttachmentType"
    video: "VideoVideo"


class WallCommentAttachmentType(enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"


class WallGeo(PydanticModel):
    coordinates: str
    place: "BasePlace"
    showmap: int
    type: str


class WallGraffiti(PydanticModel):
    id: int
    owner_id: int
    photo_200: str
    photo_586: str


class WallPostCopyright(PydanticModel):
    id: int
    link: str
    name: str
    type: str


class WallPostSource(PydanticModel):
    data: str
    platform: str
    type: "WallPostSourceType"
    url: str


class WallPostSourceType(enum.Enum):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class WallPostType(enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"


class WallPostedPhoto(PydanticModel):
    id: int
    owner_id: int
    photo_130: str
    photo_604: str


class WallViews(PydanticModel):
    count: int


class WallWallComment(PydanticModel):
    attachments: List["WallCommentAttachment"]
    date: int
    donut: "WallWallCommentDonut"
    from_id: int
    id: int
    likes: "BaseLikesInfo"
    real_offset: int
    reply_to_comment: int
    reply_to_user: int
    text: str
    thread: "CommentThread"
    post_id: int
    owner_id: int
    parents_stack: List[int]
    deleted: bool


class WallWallCommentDonut(PydanticModel):
    is_don: bool
    placeholder: "WallWallCommentDonutPlaceholder"


class WallWallCommentDonutPlaceholder(PydanticModel):
    text: str


class WallWallpost(PydanticModel):
    access_key: str
    attachments: List["WallWallpostAttachment"]
    copyright: "WallPostCopyright"
    date: int
    edited: int
    from_id: int
    geo: "WallGeo"
    id: int
    is_archived: bool
    is_favorite: bool
    likes: "BaseLikesInfo"
    owner_id: int
    poster: object
    post_id: int
    parents_stack: List[int]
    post_source: "WallPostSource"
    post_type: "WallPostType"
    reposts: "BaseRepostsInfo"
    signer_id: int
    text: str
    views: "WallViews"


class WallWallpostAttachment(PydanticModel):
    access_key: str
    album: "PhotosPhotoAlbum"
    app: "WallAppPost"
    audio: "AudioAudio"
    doc: "DocsDoc"
    event: "EventsEventAttach"
    group: "GroupsGroupAttach"
    graffiti: "WallGraffiti"
    link: "BaseLink"
    market: "MarketMarketItem"
    market_album: "MarketMarketAlbum"
    note: "WallAttachedNote"
    page: "PagesWikipageFull"
    photo: "PhotosPhoto"
    photos_list: List[str]
    poll: "PollsPoll"
    posted_photo: "WallPostedPhoto"
    type: "WallWallpostAttachmentType"
    video: "VideoVideo"


class WallWallpostAttachmentType(enum.Enum):
    PHOTO = "photo"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    EVENT = "event"


class WallWallpostCommentsDonut(PydanticModel):
    placeholder: "WallWallpostCommentsDonutPlaceholder"


class WallWallpostCommentsDonutPlaceholder(PydanticModel):
    text: str


class WallWallpostDonut(PydanticModel):
    is_donut: bool
    paid_duration: int
    placeholder: "WallWallpostDonutPlaceholder"
    can_publish_free_copy: bool
    edit_mode: str


class WallWallpostDonutPlaceholder(PydanticModel):
    text: str


class WallWallpostFull(PydanticModel):
    allOf: Unsupported


class WallWallpostToId(PydanticModel):
    attachments: List["WallWallpostAttachment"]
    comments: "BaseCommentsInfo"
    copy_owner_id: int
    copy_post_id: int
    date: int
    from_id: int
    geo: "WallGeo"
    id: int
    is_favorite: bool
    likes: "BaseLikesInfo"
    post_id: int
    post_source: "WallPostSource"
    post_type: "WallPostType"
    reposts: "BaseRepostsInfo"
    signer_id: int
    text: str
    to_id: int


class WidgetsCommentMedia(PydanticModel):
    item_id: int
    owner_id: int
    thumb_src: str
    type: "WidgetsCommentMediaType"


class WidgetsCommentMediaType(enum.Enum):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(PydanticModel):
    can_post: "BaseBoolInt"
    count: int
    replies: List["WidgetsCommentRepliesItem"]


class WidgetsCommentRepliesItem(PydanticModel):
    cid: int
    date: int
    likes: "WidgetsWidgetLikes"
    text: str
    uid: int
    user: "UsersUserFull"


class WidgetsWidgetComment(PydanticModel):
    attachments: List["WallCommentAttachment"]
    can_delete: "BaseBoolInt"
    comments: "WidgetsCommentReplies"
    date: int
    from_id: int
    id: int
    likes: "BaseLikesInfo"
    media: "WidgetsCommentMedia"
    post_source: "WallPostSource"
    post_type: int
    reposts: "BaseRepostsInfo"
    text: str
    to_id: int
    user: "UsersUserFull"


class WidgetsWidgetLikes(PydanticModel):
    count: int


class WidgetsWidgetPage(PydanticModel):
    comments: "BaseObjectCount"
    date: int
    description: str
    id: int
    likes: "BaseObjectCount"
    page_id: str
    photo: str
    title: str
    url: str


AccountAccountCounters.update_forward_refs()
AccountInfo.update_forward_refs()
AccountNameRequest.update_forward_refs()
AccountOffer.update_forward_refs()
AccountPushConversations.update_forward_refs()
AccountPushConversationsItem.update_forward_refs()
AccountPushParams.update_forward_refs()
AccountPushSettings.update_forward_refs()
AccountUserSettings.update_forward_refs()
AccountUserSettingsInterest.update_forward_refs()
AccountUserSettingsInterests.update_forward_refs()
AdsAccesses.update_forward_refs()
AdsAccount.update_forward_refs()
AdsAd.update_forward_refs()
AdsAdLayout.update_forward_refs()
AdsCampaign.update_forward_refs()
AdsCategory.update_forward_refs()
AdsClient.update_forward_refs()
AdsCriteria.update_forward_refs()
AdsDemoStats.update_forward_refs()
AdsDemostatsFormat.update_forward_refs()
AdsFloodStats.update_forward_refs()
AdsLinkStatus.update_forward_refs()
AdsLookalikeRequest.update_forward_refs()
AdsLookalikeRequestSaveAudienceLevel.update_forward_refs()
AdsMusician.update_forward_refs()
AdsParagraphs.update_forward_refs()
AdsPromotedPostReach.update_forward_refs()
AdsRejectReason.update_forward_refs()
AdsRules.update_forward_refs()
AdsStats.update_forward_refs()
AdsStatsAge.update_forward_refs()
AdsStatsCities.update_forward_refs()
AdsStatsFormat.update_forward_refs()
AdsStatsSex.update_forward_refs()
AdsStatsSexAge.update_forward_refs()
AdsStatsViewsTimes.update_forward_refs()
AdsTargSettings.update_forward_refs()
AdsTargStats.update_forward_refs()
AdsTargSuggestions.update_forward_refs()
AdsTargSuggestionsCities.update_forward_refs()
AdsTargSuggestionsRegions.update_forward_refs()
AdsTargSuggestionsSchools.update_forward_refs()
AdsTargetGroup.update_forward_refs()
AdsUpdateofficeusersResult.update_forward_refs()
AdsUserSpecification.update_forward_refs()
AdsUserSpecificationCutted.update_forward_refs()
AdsUsers.update_forward_refs()
AdswebGetadcategoriesResponseCategoriesCategory.update_forward_refs()
AdswebGetadunitsResponseAdUnitsAdUnit.update_forward_refs()
AdswebGetfraudhistoryResponseEntriesEntry.update_forward_refs()
AdswebGetsitesResponseSitesSite.update_forward_refs()
AdswebGetstatisticsResponseItemsItem.update_forward_refs()
AppwidgetsPhoto.update_forward_refs()
AppwidgetsPhotos.update_forward_refs()
AppsApp.update_forward_refs()
AppsAppMin.update_forward_refs()
AppsLeaderboard.update_forward_refs()
AppsScope.update_forward_refs()
AudioAudio.update_forward_refs()
BaseCity.update_forward_refs()
BaseCommentsInfo.update_forward_refs()
BaseCountry.update_forward_refs()
BaseCropPhoto.update_forward_refs()
BaseCropPhotoCrop.update_forward_refs()
BaseCropPhotoRect.update_forward_refs()
BaseError.update_forward_refs()
BaseGeo.update_forward_refs()
BaseGeoCoordinates.update_forward_refs()
BaseGradientPoint.update_forward_refs()
BaseImage.update_forward_refs()
BaseLikes.update_forward_refs()
BaseLikesInfo.update_forward_refs()
BaseLink.update_forward_refs()
BaseLinkApplication.update_forward_refs()
BaseLinkApplicationStore.update_forward_refs()
BaseLinkButton.update_forward_refs()
BaseLinkButtonAction.update_forward_refs()
BaseLinkProduct.update_forward_refs()
BaseLinkRating.update_forward_refs()
BaseMessageError.update_forward_refs()
BaseObject.update_forward_refs()
BaseObjectCount.update_forward_refs()
BaseObjectWithName.update_forward_refs()
BasePlace.update_forward_refs()
BaseRepostsInfo.update_forward_refs()
BaseRequestParam.update_forward_refs()
BaseSticker.update_forward_refs()
BaseStickerAnimation.update_forward_refs()
BaseUploadServer.update_forward_refs()
BaseUserId.update_forward_refs()
BoardTopic.update_forward_refs()
BoardTopicComment.update_forward_refs()
BoardTopicPoll.update_forward_refs()
CallbackBoardPostDelete.update_forward_refs()
CallbackConfirmationMessage.update_forward_refs()
CallbackDonutMoneyWithdraw.update_forward_refs()
CallbackDonutMoneyWithdrawError.update_forward_refs()
CallbackDonutSubscriptionCancelled.update_forward_refs()
CallbackDonutSubscriptionCreate.update_forward_refs()
CallbackDonutSubscriptionExpired.update_forward_refs()
CallbackDonutSubscriptionPriceChanged.update_forward_refs()
CallbackDonutSubscriptionProlonged.update_forward_refs()
CallbackGroupChangePhoto.update_forward_refs()
CallbackGroupChangeSettings.update_forward_refs()
CallbackGroupJoin.update_forward_refs()
CallbackGroupLeave.update_forward_refs()
CallbackGroupOfficersEdit.update_forward_refs()
CallbackGroupSettingsChanges.update_forward_refs()
CallbackLikeAddRemove.update_forward_refs()
CallbackMarketComment.update_forward_refs()
CallbackMarketCommentDelete.update_forward_refs()
CallbackMessageAllow.update_forward_refs()
CallbackMessageBase.update_forward_refs()
CallbackMessageDeny.update_forward_refs()
CallbackPhotoComment.update_forward_refs()
CallbackPhotoCommentDelete.update_forward_refs()
CallbackPollVoteNew.update_forward_refs()
CallbackQrScan.update_forward_refs()
CallbackUserBlock.update_forward_refs()
CallbackUserUnblock.update_forward_refs()
CallbackVideoComment.update_forward_refs()
CallbackVideoCommentDelete.update_forward_refs()
CallbackWallCommentDelete.update_forward_refs()
CallsCall.update_forward_refs()
CallsParticipants.update_forward_refs()
CommentThread.update_forward_refs()
DatabaseCity.update_forward_refs()
DatabaseFaculty.update_forward_refs()
DatabaseRegion.update_forward_refs()
DatabaseSchool.update_forward_refs()
DatabaseStation.update_forward_refs()
DatabaseUniversity.update_forward_refs()
DocsDoc.update_forward_refs()
DocsDocPreview.update_forward_refs()
DocsDocPreviewAudioMsg.update_forward_refs()
DocsDocPreviewGraffiti.update_forward_refs()
DocsDocPreviewPhoto.update_forward_refs()
DocsDocPreviewPhotoSizes.update_forward_refs()
DocsDocPreviewVideo.update_forward_refs()
DocsDocTypes.update_forward_refs()
DocsDocUploadResponse.update_forward_refs()
DonutDonatorSubscriptionInfo.update_forward_refs()
EventsEventAttach.update_forward_refs()
FaveBookmark.update_forward_refs()
FavePage.update_forward_refs()
FaveTag.update_forward_refs()
FriendsFriendExtendedStatus.update_forward_refs()
FriendsFriendStatus.update_forward_refs()
FriendsFriendsList.update_forward_refs()
FriendsMutualFriend.update_forward_refs()
FriendsRequests.update_forward_refs()
FriendsRequestsMutual.update_forward_refs()
FriendsRequestsXtrMessage.update_forward_refs()
FriendsUserXtrLists.update_forward_refs()
FriendsUserXtrPhone.update_forward_refs()
GiftsGift.update_forward_refs()
GiftsLayout.update_forward_refs()
GroupsAddress.update_forward_refs()
GroupsAddressTimetable.update_forward_refs()
GroupsAddressTimetableDay.update_forward_refs()
GroupsAddressesInfo.update_forward_refs()
GroupsBanInfo.update_forward_refs()
GroupsCallbackServer.update_forward_refs()
GroupsCallbackSettings.update_forward_refs()
GroupsContactsItem.update_forward_refs()
GroupsCountersGroup.update_forward_refs()
GroupsCover.update_forward_refs()
GroupsGroup.update_forward_refs()
GroupsGroupAttach.update_forward_refs()
GroupsGroupBanInfo.update_forward_refs()
GroupsGroupCategory.update_forward_refs()
GroupsGroupCategoryFull.update_forward_refs()
GroupsGroupCategoryType.update_forward_refs()
GroupsGroupFull.update_forward_refs()
GroupsGroupLink.update_forward_refs()
GroupsGroupPublicCategoryList.update_forward_refs()
GroupsGroupTag.update_forward_refs()
GroupsGroupsArray.update_forward_refs()
GroupsLinksItem.update_forward_refs()
GroupsLiveCovers.update_forward_refs()
GroupsLongPollEvents.update_forward_refs()
GroupsLongPollServer.update_forward_refs()
GroupsLongPollSettings.update_forward_refs()
GroupsMarketInfo.update_forward_refs()
GroupsMemberRole.update_forward_refs()
GroupsMemberStatus.update_forward_refs()
GroupsMemberStatusFull.update_forward_refs()
GroupsOnlineStatus.update_forward_refs()
GroupsOwnerXtrBanInfo.update_forward_refs()
GroupsProfileItem.update_forward_refs()
GroupsSettingsTwitter.update_forward_refs()
GroupsSubjectItem.update_forward_refs()
GroupsTokenPermissionSetting.update_forward_refs()
GroupsUserXtrRole.update_forward_refs()
LinkTargetObject.update_forward_refs()
MarketCurrency.update_forward_refs()
MarketMarketAlbum.update_forward_refs()
MarketMarketCategoryNested.update_forward_refs()
MarketMarketCategoryOld.update_forward_refs()
MarketMarketCategoryTree.update_forward_refs()
MarketMarketItem.update_forward_refs()
MarketMarketItemFull.update_forward_refs()
MarketOrder.update_forward_refs()
MarketOrderItem.update_forward_refs()
MarketPrice.update_forward_refs()
MarketSection.update_forward_refs()
MediaRestriction.update_forward_refs()
MessagesAudioMessage.update_forward_refs()
MessagesChat.update_forward_refs()
MessagesChatFull.update_forward_refs()
MessagesChatPreview.update_forward_refs()
MessagesChatPushSettings.update_forward_refs()
MessagesChatRestrictions.update_forward_refs()
MessagesChatSettings.update_forward_refs()
MessagesChatSettingsAcl.update_forward_refs()
MessagesChatSettingsPermissions.update_forward_refs()
MessagesChatSettingsPhoto.update_forward_refs()
MessagesConversation.update_forward_refs()
MessagesConversationCanWrite.update_forward_refs()
MessagesConversationMember.update_forward_refs()
MessagesConversationPeer.update_forward_refs()
MessagesConversationSortId.update_forward_refs()
MessagesConversationWithMessage.update_forward_refs()
MessagesForeignMessage.update_forward_refs()
MessagesForward.update_forward_refs()
MessagesGraffiti.update_forward_refs()
MessagesHistoryAttachment.update_forward_refs()
MessagesHistoryMessageAttachment.update_forward_refs()
MessagesKeyboard.update_forward_refs()
MessagesKeyboardButton.update_forward_refs()
MessagesKeyboardButtonAction.update_forward_refs()
MessagesLastActivity.update_forward_refs()
MessagesLongpollMessages.update_forward_refs()
MessagesLongpollParams.update_forward_refs()
MessagesMessage.update_forward_refs()
MessagesMessageAction.update_forward_refs()
MessagesMessageActionPhoto.update_forward_refs()
MessagesMessageAttachment.update_forward_refs()
MessagesMessageRequestData.update_forward_refs()
MessagesMessagesArray.update_forward_refs()
MessagesOutReadBy.update_forward_refs()
MessagesPinnedMessage.update_forward_refs()
MessagesPushSettings.update_forward_refs()
MessagesUserXtrInvitedBy.update_forward_refs()
NewsfeedEventActivity.update_forward_refs()
NewsfeedItemAudio.update_forward_refs()
NewsfeedItemAudioAudio.update_forward_refs()
NewsfeedItemBase.update_forward_refs()
NewsfeedItemDigest.update_forward_refs()
NewsfeedItemDigestButton.update_forward_refs()
NewsfeedItemDigestFooter.update_forward_refs()
NewsfeedItemDigestFullItem.update_forward_refs()
NewsfeedItemDigestHeader.update_forward_refs()
NewsfeedItemFriend.update_forward_refs()
NewsfeedItemFriendFriends.update_forward_refs()
NewsfeedItemHolidayRecommendationsBlockHeader.update_forward_refs()
NewsfeedItemPhoto.update_forward_refs()
NewsfeedItemPhotoPhotos.update_forward_refs()
NewsfeedItemPhotoTag.update_forward_refs()
NewsfeedItemPhotoTagPhotoTags.update_forward_refs()
NewsfeedItemPromoButton.update_forward_refs()
NewsfeedItemPromoButtonAction.update_forward_refs()
NewsfeedItemPromoButtonImage.update_forward_refs()
NewsfeedItemTopic.update_forward_refs()
NewsfeedItemVideo.update_forward_refs()
NewsfeedItemVideoVideo.update_forward_refs()
NewsfeedItemWallpost.update_forward_refs()
NewsfeedItemWallpostFeedback.update_forward_refs()
NewsfeedItemWallpostFeedbackAnswer.update_forward_refs()
NewsfeedList.update_forward_refs()
NewsfeedListFull.update_forward_refs()
NewsfeedNewsfeedItem.update_forward_refs()
NewsfeedNewsfeedPhoto.update_forward_refs()
NotesNote.update_forward_refs()
NotesNoteComment.update_forward_refs()
NotificationsFeedback.update_forward_refs()
NotificationsNotification.update_forward_refs()
NotificationsNotificationItem.update_forward_refs()
NotificationsNotificationParent.update_forward_refs()
NotificationsNotificationsComment.update_forward_refs()
NotificationsReply.update_forward_refs()
NotificationsSendMessageError.update_forward_refs()
NotificationsSendMessageItem.update_forward_refs()
OauthError.update_forward_refs()
OrdersAmount.update_forward_refs()
OrdersAmountItem.update_forward_refs()
OrdersOrder.update_forward_refs()
OrdersSubscription.update_forward_refs()
OwnerState.update_forward_refs()
PagesWikipage.update_forward_refs()
PagesWikipageFull.update_forward_refs()
PagesWikipageHistory.update_forward_refs()
PhotosCommentXtrPid.update_forward_refs()
PhotosImage.update_forward_refs()
PhotosMarketAlbumUploadResponse.update_forward_refs()
PhotosMarketUploadResponse.update_forward_refs()
PhotosMessageUploadResponse.update_forward_refs()
PhotosOwnerUploadResponse.update_forward_refs()
PhotosPhoto.update_forward_refs()
PhotosPhotoAlbum.update_forward_refs()
PhotosPhotoAlbumFull.update_forward_refs()
PhotosPhotoFalseable.update_forward_refs()
PhotosPhotoFull.update_forward_refs()
PhotosPhotoFullXtrRealOffset.update_forward_refs()
PhotosPhotoSizes.update_forward_refs()
PhotosPhotoTag.update_forward_refs()
PhotosPhotoUpload.update_forward_refs()
PhotosPhotoUploadResponse.update_forward_refs()
PhotosPhotoXtrRealOffset.update_forward_refs()
PhotosPhotoXtrTagInfo.update_forward_refs()
PhotosTagsSuggestionItem.update_forward_refs()
PhotosTagsSuggestionItemButton.update_forward_refs()
PhotosWallUploadResponse.update_forward_refs()
PollsAnswer.update_forward_refs()
PollsBackground.update_forward_refs()
PollsFriend.update_forward_refs()
PollsPoll.update_forward_refs()
PollsVoters.update_forward_refs()
PollsVotersUsers.update_forward_refs()
PrettycardsPrettycard.update_forward_refs()
SearchHint.update_forward_refs()
SecureLevel.update_forward_refs()
SecureSmsNotification.update_forward_refs()
SecureTokenChecked.update_forward_refs()
SecureTransaction.update_forward_refs()
StatsActivity.update_forward_refs()
StatsCity.update_forward_refs()
StatsCountry.update_forward_refs()
StatsPeriod.update_forward_refs()
StatsReach.update_forward_refs()
StatsSexAge.update_forward_refs()
StatsViews.update_forward_refs()
StatsWallpostStat.update_forward_refs()
StatusStatus.update_forward_refs()
StorageValue.update_forward_refs()
StoreProduct.update_forward_refs()
StoreStickersKeyword.update_forward_refs()
StoreStickersKeywordSticker.update_forward_refs()
StoriesClickableArea.update_forward_refs()
StoriesClickableSticker.update_forward_refs()
StoriesClickableStickers.update_forward_refs()
StoriesFeedItem.update_forward_refs()
StoriesPromoBlock.update_forward_refs()
StoriesReplies.update_forward_refs()
StoriesStatLine.update_forward_refs()
StoriesStory.update_forward_refs()
StoriesStoryLink.update_forward_refs()
StoriesStoryStats.update_forward_refs()
StoriesStoryStatsStat.update_forward_refs()
StoriesViewersItem.update_forward_refs()
UsersCareer.update_forward_refs()
UsersExports.update_forward_refs()
UsersLastSeen.update_forward_refs()
UsersMilitary.update_forward_refs()
UsersOccupation.update_forward_refs()
UsersOnlineInfo.update_forward_refs()
UsersPersonal.update_forward_refs()
UsersRelative.update_forward_refs()
UsersSchool.update_forward_refs()
UsersSubscriptionsItem.update_forward_refs()
UsersUniversity.update_forward_refs()
UsersUser.update_forward_refs()
UsersUserConnections.update_forward_refs()
UsersUserCounters.update_forward_refs()
UsersUserFull.update_forward_refs()
UsersUserMin.update_forward_refs()
UsersUserSettingsXtr.update_forward_refs()
UsersUserXtrCounters.update_forward_refs()
UsersUserXtrType.update_forward_refs()
UsersUsersArray.update_forward_refs()
UtilsDomainResolved.update_forward_refs()
UtilsLastShortenedLink.update_forward_refs()
UtilsLinkChecked.update_forward_refs()
UtilsLinkStats.update_forward_refs()
UtilsLinkStatsExtended.update_forward_refs()
UtilsShortLink.update_forward_refs()
UtilsStats.update_forward_refs()
UtilsStatsCity.update_forward_refs()
UtilsStatsCountry.update_forward_refs()
UtilsStatsExtended.update_forward_refs()
UtilsStatsSexAge.update_forward_refs()
VideoLiveInfo.update_forward_refs()
VideoLiveSettings.update_forward_refs()
VideoRestrictionButton.update_forward_refs()
VideoSaveResult.update_forward_refs()
VideoVideo.update_forward_refs()
VideoVideoAlbumFull.update_forward_refs()
VideoVideoFiles.update_forward_refs()
VideoVideoFull.update_forward_refs()
VideoVideoImage.update_forward_refs()
WallAppPost.update_forward_refs()
WallAttachedNote.update_forward_refs()
WallCarouselBase.update_forward_refs()
WallCommentAttachment.update_forward_refs()
WallGeo.update_forward_refs()
WallGraffiti.update_forward_refs()
WallPostCopyright.update_forward_refs()
WallPostSource.update_forward_refs()
WallPostedPhoto.update_forward_refs()
WallViews.update_forward_refs()
WallWallComment.update_forward_refs()
WallWallCommentDonut.update_forward_refs()
WallWallCommentDonutPlaceholder.update_forward_refs()
WallWallpost.update_forward_refs()
WallWallpostAttachment.update_forward_refs()
WallWallpostCommentsDonut.update_forward_refs()
WallWallpostCommentsDonutPlaceholder.update_forward_refs()
WallWallpostDonut.update_forward_refs()
WallWallpostDonutPlaceholder.update_forward_refs()
WallWallpostFull.update_forward_refs()
WallWallpostToId.update_forward_refs()
WidgetsCommentMedia.update_forward_refs()
WidgetsCommentReplies.update_forward_refs()
WidgetsCommentRepliesItem.update_forward_refs()
WidgetsWidgetComment.update_forward_refs()
WidgetsWidgetLikes.update_forward_refs()
WidgetsWidgetPage.update_forward_refs()