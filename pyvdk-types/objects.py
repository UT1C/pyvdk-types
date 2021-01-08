from typing import Optional, Union, Any, List, Tuple
import enum

from pydantic import BaseModel as PydanticModel


class AccountAccountCounters(PydanticModel):
    app_requests: Optional[int] = None
    events: Optional[int] = None
    faves: Optional[int] = None
    friends: Optional[int] = None
    friends_suggestions: Optional[int] = None
    friends_recommendations: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    menu_discover_badge: Optional[int] = None
    menu_clips_badge: Optional[int] = None
    messages: Optional[int] = None
    memories: Optional[int] = None
    notes: Optional[int] = None
    notifications: Optional[int] = None
    photos: Optional[int] = None
    sdk: Optional[int] = None


class AccountInfo(PydanticModel):
    wishlists_ae_promo_banner_show: Optional["BaseBoolInt"] = None
    _2fa_required: Optional["BaseBoolInt"] = None
    country: Optional[str] = None
    https_required: Optional["BaseBoolInt"] = None
    intro: Optional["BaseBoolInt"] = None
    show_vk_apps_intro: Optional[bool] = None
    mini_apps_ads_slot_id: Optional[int] = None
    qr_promotion: Optional[int] = None
    link_redirects: Optional[dict] = None
    lang: Optional[int] = None
    no_wall_replies: Optional["BaseBoolInt"] = None
    own_posts_default: Optional["BaseBoolInt"] = None
    subscriptions: Optional[List[int]] = None


class AccountNameRequest(PydanticModel):
    first_name: Optional[str] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    status: Optional["AccountNameRequestStatus"] = None
    lang: Optional[str] = None
    link_href: Optional[str] = None
    link_label: Optional[str] = None


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
    description: Optional[str] = None
    id: Optional[int] = None
    img: Optional[str] = None
    instruction: Optional[str] = None
    instruction_html: Optional[str] = None
    price: Optional[int] = None
    short_description: Optional[str] = None
    tag: Optional[str] = None
    title: Optional[str] = None
    currency_amount: Optional[int] = None
    link_id: Optional[int] = None
    link_type: Optional[str] = None


class AccountPushConversations(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["AccountPushConversationsItem"]] = None


class AccountPushConversationsItem(PydanticModel):
    disabled_until: Optional[int] = None
    peer_id: Optional[int] = None
    sound: Optional["BaseBoolInt"] = None


class AccountPushParams(PydanticModel):
    msg: Optional[List["AccountPushParamsMode"]] = None
    chat: Optional[List["AccountPushParamsMode"]] = None
    like: Optional[List["AccountPushParamsSettings"]] = None
    repost: Optional[List["AccountPushParamsSettings"]] = None
    comment: Optional[List["AccountPushParamsSettings"]] = None
    mention: Optional[List["AccountPushParamsSettings"]] = None
    reply: Optional[List["AccountPushParamsOnoff"]] = None
    new_post: Optional[List["AccountPushParamsOnoff"]] = None
    wall_post: Optional[List["AccountPushParamsOnoff"]] = None
    wall_publish: Optional[List["AccountPushParamsOnoff"]] = None
    friend: Optional[List["AccountPushParamsOnoff"]] = None
    friend_found: Optional[List["AccountPushParamsOnoff"]] = None
    friend_accepted: Optional[List["AccountPushParamsOnoff"]] = None
    group_invite: Optional[List["AccountPushParamsOnoff"]] = None
    group_accepted: Optional[List["AccountPushParamsOnoff"]] = None
    birthday: Optional[List["AccountPushParamsOnoff"]] = None
    event_soon: Optional[List["AccountPushParamsOnoff"]] = None
    app_request: Optional[List["AccountPushParamsOnoff"]] = None
    sdk_open: Optional[List["AccountPushParamsOnoff"]] = None


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
    disabled: Optional["BaseBoolInt"] = None
    disabled_until: Optional[int] = None
    settings: Optional["AccountPushParams"] = None
    conversations: Optional["AccountPushConversations"] = None


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    photo_200: Optional[str] = None
    is_service_account: Optional[bool] = None


class AccountUserSettingsInterest(PydanticModel):
    title: Optional[str] = None
    value: Optional[str] = None


class AccountUserSettingsInterests(PydanticModel):
    activities: Optional["AccountUserSettingsInterest"] = None
    interests: Optional["AccountUserSettingsInterest"] = None
    music: Optional["AccountUserSettingsInterest"] = None
    tv: Optional["AccountUserSettingsInterest"] = None
    movies: Optional["AccountUserSettingsInterest"] = None
    books: Optional["AccountUserSettingsInterest"] = None
    games: Optional["AccountUserSettingsInterest"] = None
    quotes: Optional["AccountUserSettingsInterest"] = None
    about: Optional["AccountUserSettingsInterest"] = None


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
    client_id: Optional[str] = None
    role: Optional["AdsAccessRole"] = None


class AdsAccount(PydanticModel):
    access_role: Optional["AdsAccessRole"] = None
    account_id: Optional[int] = None
    account_status: Optional["BaseBoolInt"] = None
    account_type: Optional["AdsAccountType"] = None
    account_name: Optional[str] = None
    can_view_budget: Optional[bool] = None


class AdsAccountType(enum.Enum):
    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(PydanticModel):
    ad_format: Optional[int] = None
    ad_platform: Optional[Union[int, str]] = None
    all_limit: Optional[int] = None
    approved: Optional["AdsAdApproved"] = None
    campaign_id: Optional[int] = None
    category1_id: Optional[int] = None
    category2_id: Optional[int] = None
    cost_type: Optional["AdsAdCostType"] = None
    cpc: Optional[int] = None
    cpm: Optional[int] = None
    cpa: Optional[int] = None
    ocpm: Optional[int] = None
    autobidding_max_cost: Optional[int] = None
    disclaimer_medical: Optional["BaseBoolInt"] = None
    disclaimer_specialist: Optional["BaseBoolInt"] = None
    disclaimer_supplements: Optional["BaseBoolInt"] = None
    id: Optional[int] = None
    impressions_limit: Optional[int] = None
    impressions_limited: Optional["BaseBoolInt"] = None
    name: Optional[str] = None
    status: Optional["AdsAdStatus"] = None
    video: Optional["BaseBoolInt"] = None


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
    ad_format: Optional[int] = None
    campaign_id: Optional[int] = None
    cost_type: Optional["AdsAdCostType"] = None
    description: Optional[str] = None
    id: Optional[str] = None
    image_src: Optional[str] = None
    image_src_2x: Optional[str] = None
    link_domain: Optional[str] = None
    link_url: Optional[str] = None
    preview_link: Optional[Union[int, str]] = None
    title: Optional[str] = None
    video: Optional["BaseBoolInt"] = None


class AdsAdStatus(enum.IntEnum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaign(PydanticModel):
    all_limit: Optional[str] = None
    day_limit: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    start_time: Optional[int] = None
    status: Optional["AdsCampaignStatus"] = None
    stop_time: Optional[int] = None
    type: Optional["AdsCampaignType"] = None


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
    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["BaseObjectWithName"]] = None


class AdsClient(PydanticModel):
    all_limit: Optional[str] = None
    day_limit: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class AdsCriteria(PydanticModel):
    age_from: Optional[int] = None
    age_to: Optional[int] = None
    apps: Optional[str] = None
    apps_not: Optional[str] = None
    birthday: Optional[int] = None
    cities: Optional[str] = None
    cities_not: Optional[str] = None
    country: Optional[int] = None
    districts: Optional[str] = None
    groups: Optional[str] = None
    interest_categories: Optional[str] = None
    interests: Optional[str] = None
    paying: Optional["BaseBoolInt"] = None
    positions: Optional[str] = None
    religions: Optional[str] = None
    retargeting_groups: Optional[str] = None
    retargeting_groups_not: Optional[str] = None
    school_from: Optional[int] = None
    school_to: Optional[int] = None
    schools: Optional[str] = None
    sex: Optional["AdsCriteriaSex"] = None
    stations: Optional[str] = None
    statuses: Optional[str] = None
    streets: Optional[str] = None
    travellers: Optional["BasePropertyExists"] = None
    uni_from: Optional[int] = None
    uni_to: Optional[int] = None
    user_browsers: Optional[str] = None
    user_devices: Optional[str] = None
    user_os: Optional[str] = None


class AdsCriteriaSex(enum.IntEnum):
    ANY = 0
    MALE = 1
    FEMALE = 2


class AdsDemoStats(PydanticModel):
    id: Optional[int] = None
    stats: Optional["AdsDemostatsFormat"] = None
    type: Optional["AdsObjectType"] = None


class AdsDemostatsFormat(PydanticModel):
    age: Optional[List["AdsStatsAge"]] = None
    cities: Optional[List["AdsStatsCities"]] = None
    day: Optional[str] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    sex: Optional[List["AdsStatsSex"]] = None
    sex_age: Optional[List["AdsStatsSexAge"]] = None


class AdsFloodStats(PydanticModel):
    left: Optional[int] = None
    refresh: Optional[int] = None


class AdsLinkStatus(PydanticModel):
    description: Optional[str] = None
    redirect_url: Optional[str] = None
    status: Optional[str] = None


class AdsLookalikeRequest(PydanticModel):
    id: Optional[int] = None
    create_time: Optional[int] = None
    update_time: Optional[int] = None
    scheduled_delete_time: Optional[int] = None
    status: Optional[str] = None
    source_type: Optional[str] = None
    source_retargeting_group_id: Optional[int] = None
    source_name: Optional[str] = None
    audience_count: Optional[int] = None
    save_audience_levels: Optional[List["AdsLookalikeRequestSaveAudienceLevel"]] = None


class AdsLookalikeRequestSaveAudienceLevel(PydanticModel):
    level: Optional[int] = None
    audience_count: Optional[int] = None


class AdsMusician(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class AdsObjectType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsParagraphs(PydanticModel):
    paragraph: Optional[str] = None


class AdsPromotedPostReach(PydanticModel):
    hide: Optional[int] = None
    id: Optional[int] = None
    join_group: Optional[int] = None
    links: Optional[int] = None
    reach_subscribers: Optional[int] = None
    reach_total: Optional[int] = None
    report: Optional[int] = None
    to_group: Optional[int] = None
    unsubscribe: Optional[int] = None
    video_views_100p: Optional[int] = None
    video_views_25p: Optional[int] = None
    video_views_3s: Optional[int] = None
    video_views_50p: Optional[int] = None
    video_views_75p: Optional[int] = None
    video_views_start: Optional[int] = None


class AdsRejectReason(PydanticModel):
    comment: Optional[str] = None
    rules: Optional[List["AdsRules"]] = None


class AdsRules(PydanticModel):
    paragraphs: Optional[List["AdsParagraphs"]] = None
    title: Optional[str] = None


class AdsStats(PydanticModel):
    id: Optional[int] = None
    stats: Optional["AdsStatsFormat"] = None
    type: Optional["AdsObjectType"] = None
    views_times: Optional["AdsStatsViewsTimes"] = None


class AdsStatsAge(PydanticModel):
    clicks_rate: Optional[int] = None
    impressions_rate: Optional[int] = None
    value: Optional[str] = None


class AdsStatsCities(PydanticModel):
    clicks_rate: Optional[int] = None
    impressions_rate: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class AdsStatsFormat(PydanticModel):
    clicks: Optional[int] = None
    day: Optional[str] = None
    impressions: Optional[int] = None
    join_rate: Optional[int] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    reach: Optional[int] = None
    spent: Optional[int] = None
    video_clicks_site: Optional[int] = None
    video_views: Optional[int] = None
    video_views_full: Optional[int] = None
    video_views_half: Optional[int] = None


class AdsStatsSex(PydanticModel):
    clicks_rate: Optional[int] = None
    impressions_rate: Optional[int] = None
    value: Optional["AdsStatsSexValue"] = None


class AdsStatsSexAge(PydanticModel):
    clicks_rate: Optional[int] = None
    impressions_rate: Optional[int] = None
    value: Optional[str] = None


class AdsStatsSexValue(enum.Enum):
    F = "f"
    M = "m"


class AdsStatsViewsTimes(PydanticModel):
    views_ads_times_1: Optional[int] = None
    views_ads_times_2: Optional[int] = None
    views_ads_times_3: Optional[int] = None
    views_ads_times_4: Optional[int] = None
    views_ads_times_5: Optional[str] = None
    views_ads_times_6: Optional[int] = None
    views_ads_times_7: Optional[int] = None
    views_ads_times_8: Optional[int] = None
    views_ads_times_9: Optional[int] = None
    views_ads_times_10: Optional[int] = None
    views_ads_times_11_plus: Optional[int] = None


class AdsTargSettings(AdsCriteria):
    id: Optional[int] = None
    campaign_id: Optional[int] = None


class AdsTargStats(PydanticModel):
    audience_count: Optional[int] = None
    recommended_cpc: Optional[int] = None
    recommended_cpm: Optional[int] = None
    recommended_cpc_50: Optional[int] = None
    recommended_cpm_50: Optional[int] = None
    recommended_cpc_70: Optional[int] = None
    recommended_cpm_70: Optional[int] = None
    recommended_cpc_90: Optional[int] = None
    recommended_cpm_90: Optional[int] = None


class AdsTargSuggestions(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class AdsTargSuggestionsCities(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None


class AdsTargSuggestionsRegions(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class AdsTargSuggestionsSchools(PydanticModel):
    desc: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None
    type: Optional["AdsTargSuggestionsSchoolsType"] = None


class AdsTargSuggestionsSchoolsType(enum.Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(PydanticModel):
    audience_count: Optional[int] = None
    domain: Optional[str] = None
    id: Optional[int] = None
    lifetime: Optional[int] = None
    name: Optional[str] = None
    pixel: Optional[str] = None


class AdsUpdateofficeusersResult(PydanticModel):
    user_id: Optional[int] = None
    is_success: Optional[bool] = None
    error: Optional["BaseError"] = None


class AdsUserSpecification(PydanticModel):
    user_id: Optional[int] = None
    role: Optional["AdsAccessRolePublic"] = None
    grant_access_to_all_clients: Optional[bool] = None
    client_ids: Optional[List[int]] = None
    view_budget: Optional[bool] = None


class AdsUserSpecificationCutted(PydanticModel):
    user_id: Optional[int] = None
    role: Optional["AdsAccessRolePublic"] = None
    client_id: Optional[int] = None
    view_budget: Optional[bool] = None


class AdsUsers(PydanticModel):
    accesses: Optional[List["AdsAccesses"]] = None
    user_id: Optional[int] = None


class AdswebGetadcategoriesResponseCategoriesCategory(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class AdswebGetadunitsResponseAdUnitsAdUnit(PydanticModel):
    id: Optional[int] = None
    site_id: Optional[int] = None
    name: Optional[str] = None


class AdswebGetfraudhistoryResponseEntriesEntry(PydanticModel):
    site_id: Optional[int] = None
    day: Optional[str] = None


class AdswebGetsitesResponseSitesSite(PydanticModel):
    id: Optional[int] = None
    status_user: Optional[str] = None
    status_moder: Optional[str] = None
    domains: Optional[str] = None


class AdswebGetstatisticsResponseItemsItem(PydanticModel):
    site_id: Optional[int] = None
    ad_unit_id: Optional[int] = None
    overall_count: Optional[int] = None
    months_count: Optional[int] = None
    month_min: Optional[str] = None
    month_max: Optional[str] = None
    days_count: Optional[int] = None
    day_min: Optional[str] = None
    day_max: Optional[str] = None
    hours_count: Optional[int] = None
    hour_min: Optional[str] = None
    hour_max: Optional[str] = None


class AppwidgetsPhoto(PydanticModel):
    id: Optional[str] = None
    images: Optional[List["BaseImage"]] = None


class AppwidgetsPhotos(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["AppwidgetsPhoto"]] = None


class AppsApp(AppsAppMin):
    author_url: Optional[str] = None
    banner_1120: Optional[str] = None
    banner_560: Optional[str] = None
    icon_16: Optional[str] = None
    is_new: Optional["BaseBoolInt"] = None
    push_enabled: Optional["BaseBoolInt"] = None
    screen_orientation: Optional[int] = None
    friends: Optional[List[int]] = None
    catalog_position: Optional[int] = None
    description: Optional[str] = None
    genre: Optional[str] = None
    genre_id: Optional[int] = None
    international: Optional[bool] = None
    is_in_catalog: Optional[int] = None
    leaderboard_type: Optional["AppsAppLeaderboardType"] = None
    members_count: Optional[int] = None
    platform_id: Optional[str] = None
    published_date: Optional[int] = None
    screen_name: Optional[str] = None
    section: Optional[str] = None


class AppsAppLeaderboardType(enum.IntEnum):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppsAppMin(PydanticModel):
    type: Optional["AppsAppType"] = None
    id: Optional[int] = None
    title: Optional[str] = None
    author_owner_id: Optional[int] = None
    is_installed: Optional[bool] = None
    icon_139: Optional[str] = None
    icon_150: Optional[str] = None
    icon_278: Optional[str] = None
    icon_576: Optional[str] = None
    background_loader_color: Optional[str] = None
    loader_icon: Optional[str] = None
    icon_75: Optional[str] = None


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
    level: Optional[int] = None
    points: Optional[int] = None
    score: Optional[int] = None
    user_id: Optional[int] = None


class AppsScope(PydanticModel):
    name: Optional[str] = None
    title: Optional[str] = None


class AudioAudio(PydanticModel):
    artist: Optional[str] = None
    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    duration: Optional[int] = None
    date: Optional[int] = None
    album_id: Optional[int] = None
    genre_id: Optional[int] = None
    performer: Optional[str] = None


class BaseBoolInt(enum.IntEnum):
    NO = 0
    YES = 1


class BaseCity(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class BaseCommentsInfo(PydanticModel):
    can_post: Optional["BaseBoolInt"] = None
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None
    donut: Optional["WallWallpostCommentsDonut"] = None


class BaseCountry(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class BaseCropPhoto(PydanticModel):
    photo: Optional["PhotosPhoto"] = None
    crop: Optional["BaseCropPhotoCrop"] = None
    rect: Optional["BaseCropPhotoRect"] = None


class BaseCropPhotoCrop(PydanticModel):
    x: Optional[int] = None
    y: Optional[int] = None
    x2: Optional[int] = None
    y2: Optional[int] = None


class BaseCropPhotoRect(PydanticModel):
    x: Optional[int] = None
    y: Optional[int] = None
    x2: Optional[int] = None
    y2: Optional[int] = None


class BaseError(PydanticModel):
    error_code: Optional[int] = None
    error_subcode: Optional[int] = None
    error_msg: Optional[str] = None
    error_text: Optional[str] = None
    request_params: Optional[List["BaseRequestParam"]] = None


class BaseGeo(PydanticModel):
    coordinates: Optional["BaseGeoCoordinates"] = None
    place: Optional["BasePlace"] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class BaseGeoCoordinates(PydanticModel):
    latitude: Optional[int] = None
    longitude: Optional[int] = None


class BaseGradientPoint(PydanticModel):
    color: Optional[str] = None
    position: Optional[int] = None


class BaseImage(PydanticModel):
    id: Optional[str] = None
    height: Optional[int] = None
    url: Optional[str] = None
    width: Optional[int] = None


class BaseLikes(PydanticModel):
    count: Optional[int] = None
    user_likes: Optional["BaseBoolInt"] = None


class BaseLikesInfo(PydanticModel):
    can_like: Optional["BaseBoolInt"] = None
    can_publish: Optional["BaseBoolInt"] = None
    count: Optional[int] = None
    user_likes: Optional[int] = None


class BaseLink(PydanticModel):
    application: Optional["BaseLinkApplication"] = None
    button: Optional["BaseLinkButton"] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_favorite: Optional[bool] = None
    photo: Optional["PhotosPhoto"] = None
    preview_page: Optional[str] = None
    preview_url: Optional[str] = None
    product: Optional["BaseLinkProduct"] = None
    rating: Optional["BaseLinkRating"] = None
    title: Optional[str] = None
    url: Optional[str] = None
    target_object: Optional["LinkTargetObject"] = None
    is_external: Optional[bool] = None
    video: Optional["VideoVideo"] = None


class BaseLinkApplication(PydanticModel):
    app_id: Optional[int] = None
    store: Optional["BaseLinkApplicationStore"] = None


class BaseLinkApplicationStore(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class BaseLinkButton(PydanticModel):
    action: Optional["BaseLinkButtonAction"] = None
    title: Optional[str] = None
    block_id: Optional[str] = None
    section_id: Optional[str] = None
    curator_id: Optional[int] = None
    owner_id: Optional[int] = None
    icon: Optional[str] = None
    style: Optional["BaseLinkButtonStyle"] = None


class BaseLinkButtonAction(PydanticModel):
    type: Optional["BaseLinkButtonActionType"] = None
    url: Optional[str] = None
    consume_reason: Optional[str] = None


class BaseLinkButtonActionType(enum.Enum):
    OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class BaseLinkProduct(PydanticModel):
    price: Optional["MarketPrice"] = None
    merchant: Optional[str] = None
    orders_count: Optional[int] = None


class BaseLinkProductStatus(enum.Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class BaseLinkRating(PydanticModel):
    reviews_count: Optional[int] = None
    stars: Optional[int] = None


class BaseMessageError(PydanticModel):
    code: Optional[int] = None
    description: Optional[str] = None


class BaseObject(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class BaseObjectCount(PydanticModel):
    count: Optional[int] = None


class BaseObjectWithName(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class BasePlace(PydanticModel):
    address: Optional[str] = None
    checkins: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    created: Optional[int] = None
    icon: Optional[str] = None
    id: Optional[int] = None
    latitude: Optional[int] = None
    longitude: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None


class BasePropertyExists(enum.IntEnum):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(PydanticModel):
    count: Optional[int] = None
    wall_count: Optional[int] = None
    mail_count: Optional[int] = None
    user_reposted: Optional[int] = None


class BaseRequestParam(PydanticModel):
    key: Optional[str] = None
    value: Optional[str] = None


class BaseSex(enum.IntEnum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class BaseSticker(PydanticModel):
    sticker_id: Optional[int] = None
    product_id: Optional[int] = None
    images: Optional[List["BaseImage"]] = None
    images_with_background: Optional[List["BaseImage"]] = None
    animation_url: Optional[str] = None
    animations: Optional[List["BaseStickerAnimation"]] = None
    is_allowed: Optional[bool] = None


class BaseStickerAnimation(PydanticModel):
    type: Optional[str] = None
    url: Optional[str] = None


BaseStickersList = List["BaseSticker"]


class BaseUploadServer(PydanticModel):
    upload_url: Optional[str] = None


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
    user_id: Optional[int] = None


class BoardDefaultOrder(enum.IntEnum):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class BoardTopic(PydanticModel):
    comments: Optional[int] = None
    created: Optional[int] = None
    created_by: Optional[int] = None
    id: Optional[int] = None
    is_closed: Optional["BaseBoolInt"] = None
    is_fixed: Optional["BaseBoolInt"] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    updated_by: Optional[int] = None


class BoardTopicComment(PydanticModel):
    attachments: Optional[List["WallCommentAttachment"]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    real_offset: Optional[int] = None
    text: Optional[str] = None
    can_edit: Optional["BaseBoolInt"] = None
    likes: Optional["BaseLikesInfo"] = None


class BoardTopicPoll(PydanticModel):
    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    created: Optional[int] = None
    is_closed: Optional["BaseBoolInt"] = None
    question: Optional[str] = None
    votes: Optional[int] = None
    answer_id: Optional[int] = None
    answers: Optional[List["PollsAnswer"]] = None


class CallbackBoardPostDelete(PydanticModel):
    topic_owner_id: Optional[int] = None
    topic_id: Optional[int] = None
    id: Optional[int] = None


class CallbackConfirmationMessage(PydanticModel):
    type: Optional["CallbackMessageType"] = None
    group_id: Optional[int] = None
    secret: Optional[str] = None


class CallbackDonutMoneyWithdraw(PydanticModel):
    amount: Optional[int] = None
    amount_without_fee: Optional[int] = None


class CallbackDonutMoneyWithdrawError(PydanticModel):
    reason: Optional[str] = None


class CallbackDonutSubscriptionCancelled(PydanticModel):
    user_id: Optional[int] = None


class CallbackDonutSubscriptionCreate(PydanticModel):
    user_id: Optional[int] = None
    amount: Optional[int] = None
    amount_without_fee: Optional[int] = None


class CallbackDonutSubscriptionExpired(PydanticModel):
    user_id: Optional[int] = None


class CallbackDonutSubscriptionPriceChanged(PydanticModel):
    user_id: Optional[int] = None
    amount_old: Optional[int] = None
    amount_new: Optional[int] = None
    amount_diff: Optional[int] = None
    amount_diff_without_fee: Optional[int] = None


class CallbackDonutSubscriptionProlonged(PydanticModel):
    user_id: Optional[int] = None
    amount: Optional[int] = None
    amount_without_fee: Optional[int] = None


class CallbackGroupChangePhoto(PydanticModel):
    user_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None


class CallbackGroupChangeSettings(PydanticModel):
    user_id: Optional[int] = None
    self: Optional["BaseBoolInt"] = None


class CallbackGroupJoin(PydanticModel):
    user_id: Optional[int] = None
    join_type: Optional["CallbackGroupJoinType"] = None


class CallbackGroupJoinType(enum.Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(PydanticModel):
    user_id: Optional[int] = None
    self: Optional["BaseBoolInt"] = None


class CallbackGroupMarket(enum.IntEnum):
    DISABLED = 0
    OPEN = 1


class CallbackGroupOfficerRole(enum.IntEnum):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(PydanticModel):
    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    level_old: Optional["CallbackGroupOfficerRole"] = None
    level_new: Optional["CallbackGroupOfficerRole"] = None


class CallbackGroupSettingsChanges(PydanticModel):
    title: Optional[str] = None
    description: Optional[str] = None
    access: Optional["GroupsGroupIsClosed"] = None
    screen_name: Optional[str] = None
    public_category: Optional[int] = None
    public_subcategory: Optional[int] = None
    age_limits: Optional["GroupsGroupFullAgeLimits"] = None
    website: Optional[str] = None
    enable_status_default: Optional["GroupsGroupWall"] = None
    enable_audio: Optional["GroupsGroupAudio"] = None
    enable_video: Optional["GroupsGroupVideo"] = None
    enable_photo: Optional["GroupsGroupPhotos"] = None
    enable_market: Optional["CallbackGroupMarket"] = None


class CallbackLikeAddRemove(PydanticModel):
    liker_id: Optional[int] = None
    object_type: Optional[str] = None
    object_owner_id: Optional[int] = None
    object_id: Optional[int] = None
    post_id: Optional[int] = None
    thread_reply_id: Optional[int] = None


class CallbackMarketComment(PydanticModel):
    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    market_owner_od: Optional[int] = None
    photo_id: Optional[int] = None


class CallbackMarketCommentDelete(PydanticModel):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    item_id: Optional[int] = None


class CallbackMessageAllow(PydanticModel):
    user_id: Optional[int] = None
    key: Optional[str] = None


class CallbackMessageBase(PydanticModel):
    type: Optional["CallbackMessageType"] = None
    object: Optional[dict] = None
    group_id: Optional[int] = None


class CallbackMessageDeny(PydanticModel):
    user_id: Optional[int] = None


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
    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    photo_owner_od: Optional[int] = None


class CallbackPhotoCommentDelete(PydanticModel):
    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    photo_id: Optional[int] = None


class CallbackPollVoteNew(PydanticModel):
    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    option_id: Optional[int] = None
    user_id: Optional[int] = None


class CallbackQrScan(PydanticModel):
    user_id: Optional[int] = None
    data: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    reread: Optional[bool] = None


class CallbackUserBlock(PydanticModel):
    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    unblock_date: Optional[int] = None
    reason: Optional[int] = None
    comment: Optional[str] = None


class CallbackUserUnblock(PydanticModel):
    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    by_end_date: Optional[int] = None


class CallbackVideoComment(PydanticModel):
    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    video_owner_od: Optional[int] = None


class CallbackVideoCommentDelete(PydanticModel):
    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    video_id: Optional[int] = None


class CallbackWallCommentDelete(PydanticModel):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    post_id: Optional[int] = None


class CallsCall(PydanticModel):
    duration: Optional[int] = None
    initiator_id: Optional[int] = None
    receiver_id: Optional[int] = None
    state: Optional["CallsEndState"] = None
    time: Optional[int] = None
    video: Optional[bool] = None


class CallsEndState(enum.Enum):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class CallsParticipants(PydanticModel):
    list: Optional[List[int]] = None
    count: Optional[int] = None


class CommentThread(PydanticModel):
    can_post: Optional[bool] = None
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None
    items: Optional[List["WallWallComment"]] = None
    show_reply_button: Optional[bool] = None


class DatabaseCity(BaseObject):
    area: Optional[str] = None
    region: Optional[str] = None
    important: Optional["BaseBoolInt"] = None


class DatabaseFaculty(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class DatabaseRegion(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class DatabaseSchool(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class DatabaseStation(PydanticModel):
    city_id: Optional[int] = None
    color: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class DatabaseUniversity(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class DocsDoc(PydanticModel):
    id: Optional[int] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    size: Optional[int] = None
    ext: Optional[str] = None
    url: Optional[str] = None
    date: Optional[int] = None
    type: Optional[int] = None
    preview: Optional["DocsDocPreview"] = None
    is_licensed: Optional["BaseBoolInt"] = None
    access_key: Optional[str] = None
    tags: Optional[List[str]] = None


class DocsDocAttachmentType(enum.Enum):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(PydanticModel):
    audio_msg: Optional["DocsDocPreviewAudioMsg"] = None
    graffiti: Optional["DocsDocPreviewGraffiti"] = None
    photo: Optional["DocsDocPreviewPhoto"] = None
    video: Optional["DocsDocPreviewVideo"] = None


class DocsDocPreviewAudioMsg(PydanticModel):
    duration: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    waveform: Optional[List[int]] = None


class DocsDocPreviewGraffiti(PydanticModel):
    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class DocsDocPreviewPhoto(PydanticModel):
    sizes: Optional[List["DocsDocPreviewPhotoSizes"]] = None


class DocsDocPreviewPhotoSizes(PydanticModel):
    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    type: Optional["PhotosPhotoSizesType"] = None


class DocsDocPreviewVideo(PydanticModel):
    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None


class DocsDocTypes(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    count: Optional[int] = None


class DocsDocUploadResponse(PydanticModel):
    file: Optional[str] = None


class DonutDonatorSubscriptionInfo(PydanticModel):
    owner_id: Optional[int] = None
    next_payment_date: Optional[int] = None
    amount: Optional[int] = None
    status: Optional[str] = None


class EventsEventAttach(PydanticModel):
    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    text: Optional[str] = None
    time: Optional[int] = None


class FaveBookmark(PydanticModel):
    added_date: Optional[int] = None
    link: Optional["BaseLink"] = None
    post: Optional["WallWallpostFull"] = None
    product: Optional["MarketMarketItem"] = None
    seen: Optional[bool] = None
    tags: Optional[List["FaveTag"]] = None
    type: Optional["FaveBookmarkType"] = None
    video: Optional["VideoVideo"] = None


class FaveBookmarkType(enum.Enum):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class FavePage(PydanticModel):
    description: Optional[str] = None
    group: Optional["GroupsGroupFull"] = None
    tags: Optional[List["FaveTag"]] = None
    type: Optional["FavePageType"] = None
    updated_date: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class FavePageType(enum.Enum):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    is_request_unread: Optional[bool] = None


class FriendsFriendStatus(PydanticModel):
    friend_status: Optional["FriendsFriendStatusStatus"] = None
    sign: Optional[str] = None
    user_id: Optional[int] = None


class FriendsFriendStatusStatus(enum.IntEnum):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsFriendsList(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class FriendsMutualFriend(PydanticModel):
    common_count: Optional[int] = None
    common_friends: Optional[List[int]] = None
    id: Optional[int] = None


class FriendsRequests(PydanticModel):
    _from: Optional[str] = None
    mutual: Optional["FriendsRequestsMutual"] = None
    user_id: Optional[int] = None


class FriendsRequestsMutual(PydanticModel):
    count: Optional[int] = None
    users: Optional[List[int]] = None


class FriendsRequestsXtrMessage(PydanticModel):
    _from: Optional[str] = None
    message: Optional[str] = None
    mutual: Optional["FriendsRequestsMutual"] = None
    user_id: Optional[int] = None


class FriendsUserXtrLists(UsersUserFull):
    lists: Optional[List[int]] = None


class FriendsUserXtrPhone(UsersUserFull):
    phone: Optional[str] = None


class GiftsGift(PydanticModel):
    date: Optional[int] = None
    from_id: Optional[int] = None
    gift: Optional["GiftsLayout"] = None
    gift_hash: Optional[str] = None
    id: Optional[int] = None
    message: Optional[str] = None
    privacy: Optional["GiftsGiftPrivacy"] = None


class GiftsGiftPrivacy(enum.IntEnum):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(PydanticModel):
    id: Optional[int] = None
    thumb_512: Optional[str] = None
    thumb_256: Optional[str] = None
    thumb_48: Optional[str] = None
    thumb_96: Optional[str] = None
    stickers_product_id: Optional[int] = None
    is_stickers_style: Optional[bool] = None
    build_id: Optional[str] = None
    keywords: Optional[str] = None


class GroupsAddress(PydanticModel):
    additional_address: Optional[str] = None
    address: Optional[str] = None
    city_id: Optional[int] = None
    country_id: Optional[int] = None
    distance: Optional[int] = None
    id: Optional[int] = None
    latitude: Optional[int] = None
    longitude: Optional[int] = None
    metro_station_id: Optional[int] = None
    phone: Optional[str] = None
    time_offset: Optional[int] = None
    timetable: Optional["GroupsAddressTimetable"] = None
    title: Optional[str] = None
    work_info_status: Optional["GroupsAddressWorkInfoStatus"] = None


class GroupsAddressTimetable(PydanticModel):
    fri: Optional["GroupsAddressTimetableDay"] = None
    mon: Optional["GroupsAddressTimetableDay"] = None
    sat: Optional["GroupsAddressTimetableDay"] = None
    sun: Optional["GroupsAddressTimetableDay"] = None
    thu: Optional["GroupsAddressTimetableDay"] = None
    tue: Optional["GroupsAddressTimetableDay"] = None
    wed: Optional["GroupsAddressTimetableDay"] = None


class GroupsAddressTimetableDay(PydanticModel):
    break_close_time: Optional[int] = None
    break_open_time: Optional[int] = None
    close_time: Optional[int] = None
    open_time: Optional[int] = None


class GroupsAddressWorkInfoStatus(enum.Enum):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(PydanticModel):
    is_enabled: Optional[bool] = None
    main_address_id: Optional[int] = None


class GroupsBanInfo(PydanticModel):
    admin_id: Optional[int] = None
    comment: Optional[str] = None
    comment_visible: Optional[bool] = None
    is_closed: Optional[bool] = None
    date: Optional[int] = None
    end_date: Optional[int] = None
    reason: Optional["GroupsBanInfoReason"] = None


class GroupsBanInfoReason(enum.IntEnum):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


GroupsBannedItem = GroupsOwnerXtrBanInfo


class GroupsCallbackServer(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None
    creator_id: Optional[int] = None
    url: Optional[str] = None
    secret_key: Optional[str] = None
    status: Optional[str] = None


class GroupsCallbackSettings(PydanticModel):
    api_version: Optional[str] = None
    events: Optional["GroupsLongPollEvents"] = None


class GroupsContactsItem(PydanticModel):
    user_id: Optional[int] = None
    desc: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class GroupsCountersGroup(PydanticModel):
    addresses: Optional[int] = None
    albums: Optional[int] = None
    audios: Optional[int] = None
    audio_playlists: Optional[int] = None
    docs: Optional[int] = None
    market: Optional[int] = None
    photos: Optional[int] = None
    topics: Optional[int] = None
    videos: Optional[int] = None


class GroupsCover(PydanticModel):
    enabled: Optional["BaseBoolInt"] = None
    images: Optional[List["BaseImage"]] = None


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
    id: Optional[int] = None
    name: Optional[str] = None
    screen_name: Optional[str] = None
    is_closed: Optional["GroupsGroupIsClosed"] = None
    type: Optional["GroupsGroupType"] = None
    is_admin: Optional["BaseBoolInt"] = None
    admin_level: Optional["GroupsGroupAdminLevel"] = None
    is_member: Optional["BaseBoolInt"] = None
    is_advertiser: Optional["BaseBoolInt"] = None
    start_date: Optional[int] = None
    finish_date: Optional[int] = None
    deactivated: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None


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
    id: Optional[int] = None
    text: Optional[str] = None
    status: Optional[str] = None
    size: Optional[int] = None
    is_favorite: Optional[bool] = None


class GroupsGroupAudio(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupBanInfo(PydanticModel):
    comment: Optional[str] = None
    end_date: Optional[int] = None
    reason: Optional["GroupsBanInfoReason"] = None


class GroupsGroupCategory(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["BaseObjectWithName"]] = None


class GroupsGroupCategoryFull(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    page_count: Optional[int] = None
    page_previews: Optional[List["GroupsGroup"]] = None
    subcategories: Optional[List["GroupsGroupCategory"]] = None


class GroupsGroupCategoryType(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class GroupsGroupDocs(enum.IntEnum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupFull(GroupsGroup):
    market: Optional["GroupsMarketInfo"] = None
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    is_adult: Optional["BaseBoolInt"] = None
    is_hidden_from_feed: Optional["BaseBoolInt"] = None
    is_favorite: Optional["BaseBoolInt"] = None
    is_subscribed: Optional["BaseBoolInt"] = None
    city: Optional["BaseObject"] = None
    country: Optional["BaseCountry"] = None
    verified: Optional["BaseBoolInt"] = None
    description: Optional[str] = None
    wiki_page: Optional[str] = None
    members_count: Optional[int] = None
    requests_count: Optional[int] = None
    video_live_level: Optional[int] = None
    video_live_count: Optional[int] = None
    clips_count: Optional[int] = None
    counters: Optional["GroupsCountersGroup"] = None
    cover: Optional["GroupsCover"] = None
    can_post: Optional["BaseBoolInt"] = None
    can_suggest: Optional["BaseBoolInt"] = None
    can_upload_story: Optional["BaseBoolInt"] = None
    can_upload_doc: Optional["BaseBoolInt"] = None
    can_upload_video: Optional["BaseBoolInt"] = None
    can_see_all_posts: Optional["BaseBoolInt"] = None
    can_create_topic: Optional["BaseBoolInt"] = None
    activity: Optional[str] = None
    fixed_post: Optional[int] = None
    has_photo: Optional["BaseBoolInt"] = None
    crop_photo: Optional["BaseCropPhoto"] = None
    status: Optional[str] = None
    status_audio: Optional["AudioAudio"] = None
    main_album_id: Optional[int] = None
    links: Optional[List["GroupsLinksItem"]] = None
    contacts: Optional[List["GroupsContactsItem"]] = None
    wall: Optional[int] = None
    site: Optional[str] = None
    main_section: Optional["GroupsGroupFullMainSection"] = None
    secondary_section: Optional[int] = None
    trending: Optional["BaseBoolInt"] = None
    can_message: Optional["BaseBoolInt"] = None
    is_messages_blocked: Optional["BaseBoolInt"] = None
    can_send_notify: Optional["BaseBoolInt"] = None
    online_status: Optional["GroupsOnlineStatus"] = None
    invited_by: Optional[int] = None
    age_limits: Optional["GroupsGroupFullAgeLimits"] = None
    ban_info: Optional["GroupsGroupBanInfo"] = None
    has_market_app: Optional[bool] = None
    using_vkpay_market_app: Optional[bool] = None
    has_group_channel: Optional[bool] = None
    addresses: Optional["GroupsAddressesInfo"] = None
    is_subscribed_podcasts: Optional[bool] = None
    can_subscribe_podcasts: Optional[bool] = None
    can_subscribe_posts: Optional[bool] = None
    live_covers: Optional["GroupsLiveCovers"] = None
    stories_archive_count: Optional[int] = None


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
    name: Optional[str] = None
    desc: Optional[str] = None
    edit_title: Optional["BaseBoolInt"] = None
    id: Optional[int] = None
    image_processing: Optional["BaseBoolInt"] = None
    url: Optional[str] = None


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
    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["GroupsGroupCategoryType"]] = None


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
    id: Optional[int] = None
    name: Optional[str] = None
    color: Optional[str] = None
    uses: Optional[int] = None


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
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GroupsLinksItem(PydanticModel):
    desc: Optional[str] = None
    edit_title: Optional["BaseBoolInt"] = None
    id: Optional[int] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_50: Optional[str] = None
    url: Optional[str] = None


class GroupsLiveCovers(PydanticModel):
    is_enabled: Optional[bool] = None
    is_scalable: Optional[bool] = None
    story_ids: Optional[List[str]] = None


class GroupsLongPollEvents(PydanticModel):
    audio_new: Optional["BaseBoolInt"] = None
    board_post_delete: Optional["BaseBoolInt"] = None
    board_post_edit: Optional["BaseBoolInt"] = None
    board_post_new: Optional["BaseBoolInt"] = None
    board_post_restore: Optional["BaseBoolInt"] = None
    group_change_photo: Optional["BaseBoolInt"] = None
    group_change_settings: Optional["BaseBoolInt"] = None
    group_join: Optional["BaseBoolInt"] = None
    group_leave: Optional["BaseBoolInt"] = None
    group_officers_edit: Optional["BaseBoolInt"] = None
    lead_forms_new: Optional["BaseBoolInt"] = None
    market_comment_delete: Optional["BaseBoolInt"] = None
    market_comment_edit: Optional["BaseBoolInt"] = None
    market_comment_new: Optional["BaseBoolInt"] = None
    market_comment_restore: Optional["BaseBoolInt"] = None
    market_order_new: Optional["BaseBoolInt"] = None
    market_order_edit: Optional["BaseBoolInt"] = None
    message_allow: Optional["BaseBoolInt"] = None
    message_deny: Optional["BaseBoolInt"] = None
    message_new: Optional["BaseBoolInt"] = None
    message_read: Optional["BaseBoolInt"] = None
    message_reply: Optional["BaseBoolInt"] = None
    message_typing_state: Optional["BaseBoolInt"] = None
    message_edit: Optional["BaseBoolInt"] = None
    photo_comment_delete: Optional["BaseBoolInt"] = None
    photo_comment_edit: Optional["BaseBoolInt"] = None
    photo_comment_new: Optional["BaseBoolInt"] = None
    photo_comment_restore: Optional["BaseBoolInt"] = None
    photo_new: Optional["BaseBoolInt"] = None
    poll_vote_new: Optional["BaseBoolInt"] = None
    user_block: Optional["BaseBoolInt"] = None
    user_unblock: Optional["BaseBoolInt"] = None
    video_comment_delete: Optional["BaseBoolInt"] = None
    video_comment_edit: Optional["BaseBoolInt"] = None
    video_comment_new: Optional["BaseBoolInt"] = None
    video_comment_restore: Optional["BaseBoolInt"] = None
    video_new: Optional["BaseBoolInt"] = None
    wall_post_new: Optional["BaseBoolInt"] = None
    wall_reply_delete: Optional["BaseBoolInt"] = None
    wall_reply_edit: Optional["BaseBoolInt"] = None
    wall_reply_new: Optional["BaseBoolInt"] = None
    wall_reply_restore: Optional["BaseBoolInt"] = None
    wall_repost: Optional["BaseBoolInt"] = None
    donut_subscription_create: Optional["BaseBoolInt"] = None
    donut_subscription_prolonged: Optional["BaseBoolInt"] = None
    donut_subscription_cancelled: Optional["BaseBoolInt"] = None
    donut_subscription_expired: Optional["BaseBoolInt"] = None
    donut_subscription_price_changed: Optional["BaseBoolInt"] = None
    donut_money_withdraw: Optional["BaseBoolInt"] = None
    donut_money_withdraw_error: Optional["BaseBoolInt"] = None


class GroupsLongPollServer(PydanticModel):
    key: Optional[str] = None
    server: Optional[str] = None
    ts: Optional[str] = None


class GroupsLongPollSettings(PydanticModel):
    api_version: Optional[str] = None
    events: Optional["GroupsLongPollEvents"] = None
    is_enabled: Optional[bool] = None


class GroupsMarketInfo(PydanticModel):
    contact_id: Optional[int] = None
    currency: Optional["MarketCurrency"] = None
    currency_text: Optional[str] = None
    enabled: Optional["BaseBoolInt"] = None
    main_album_id: Optional[int] = None
    price_max: Optional[str] = None
    price_min: Optional[str] = None


class GroupsMarketState(enum.Enum):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class GroupsMemberRole(PydanticModel):
    id: Optional[int] = None
    permissions: Optional[List["GroupsMemberRolePermission"]] = None
    role: Optional["GroupsMemberRoleStatus"] = None


class GroupsMemberRolePermission(enum.Enum):
    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsMemberStatus(PydanticModel):
    member: Optional["BaseBoolInt"] = None
    user_id: Optional[int] = None


class GroupsMemberStatusFull(PydanticModel):
    can_invite: Optional["BaseBoolInt"] = None
    can_recall: Optional["BaseBoolInt"] = None
    invitation: Optional["BaseBoolInt"] = None
    member: Optional["BaseBoolInt"] = None
    request: Optional["BaseBoolInt"] = None
    user_id: Optional[int] = None


class GroupsOnlineStatus(PydanticModel):
    minutes: Optional[int] = None
    status: Optional["GroupsOnlineStatusType"] = None


class GroupsOnlineStatusType(enum.Enum):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(PydanticModel):
    ban_info: Optional["GroupsBanInfo"] = None
    group: Optional["GroupsGroup"] = None
    profile: Optional["UsersUser"] = None
    type: Optional["GroupsOwnerXtrBanInfoType"] = None


class GroupsOwnerXtrBanInfoType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"


class GroupsProfileItem(PydanticModel):
    id: Optional[int] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    first_name: Optional[str] = None


class GroupsRoleOptions(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsSettingsTwitter(PydanticModel):
    status: Optional[str] = None
    name: Optional[str] = None


class GroupsSubjectItem(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class GroupsTokenPermissionSetting(PydanticModel):
    name: Optional[str] = None
    setting: Optional[int] = None


class GroupsUserXtrRole(UsersUserFull):
    role: Optional["GroupsRoleOptions"] = None


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
    type: Optional[str] = None
    owner_id: Optional[int] = None
    item_id: Optional[int] = None


class MarketCurrency(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class MarketMarketAlbum(PydanticModel):
    count: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


MarketMarketCategory = MarketMarketCategoryOld


class MarketMarketCategoryNested(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional["MarketMarketCategoryNested"] = None


class MarketMarketCategoryOld(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    section: Optional["MarketSection"] = None


class MarketMarketCategoryTree(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    children: Optional[List["MarketMarketCategoryTree"]] = None


class MarketMarketItem(PydanticModel):
    access_key: Optional[str] = None
    availability: Optional["MarketMarketItemAvailability"] = None
    button_title: Optional[str] = None
    category: Optional["MarketMarketCategory"] = None
    date: Optional[int] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    owner_id: Optional[int] = None
    price: Optional["MarketPrice"] = None
    thumb_photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    variants_grouping_id: Optional[int] = None
    is_main_variant: Optional[bool] = None


class MarketMarketItemAvailability(enum.IntEnum):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketMarketItemFull(MarketMarketItem):
    albums_ids: Optional[List[int]] = None
    photos: Optional[List["PhotosPhoto"]] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_repost: Optional["BaseBoolInt"] = None
    likes: Optional["BaseLikes"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    views_count: Optional[int] = None
    wishlist_item_id: Optional[int] = None
    cancel_info: Optional["BaseLink"] = None
    user_agreement_info: Optional[str] = None


class MarketOrder(PydanticModel):
    id: Optional[int] = None
    group_id: Optional[int] = None
    user_id: Optional[int] = None
    display_order_id: Optional[str] = None
    date: Optional[int] = None
    status: Optional[int] = None
    items_count: Optional[int] = None
    track_number: Optional[str] = None
    track_link: Optional[str] = None
    comment: Optional[str] = None
    address: Optional[str] = None
    merchant_comment: Optional[str] = None
    weight: Optional[int] = None
    total_price: Optional["MarketPrice"] = None
    preview_order_items: Optional[List["MarketOrderItem"]] = None
    cancel_info: Optional["BaseLink"] = None


class MarketOrderItem(PydanticModel):
    owner_id: Optional[int] = None
    item_id: Optional[int] = None
    price: Optional["MarketPrice"] = None
    quantity: Optional[int] = None
    item: Optional["MarketMarketItem"] = None
    title: Optional[str] = None
    photo: Optional["PhotosPhoto"] = None
    variants: Optional[List[str]] = None


class MarketPrice(PydanticModel):
    amount: Optional[str] = None
    currency: Optional["MarketCurrency"] = None
    discount_rate: Optional[int] = None
    old_amount: Optional[str] = None
    text: Optional[str] = None
    old_amount_text: Optional[str] = None


class MarketSection(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None


class MediaRestriction(PydanticModel):
    text: Optional[str] = None
    title: Optional[str] = None
    button: Optional["VideoRestrictionButton"] = None
    always_shown: Optional["BaseBoolInt"] = None
    blur: Optional["BaseBoolInt"] = None
    can_play: Optional["BaseBoolInt"] = None
    can_preview: Optional["BaseBoolInt"] = None
    card_icon: Optional[List["BaseImage"]] = None
    list_icon: Optional[List["BaseImage"]] = None


class MessagesAudioMessage(PydanticModel):
    access_key: Optional[str] = None
    transcript_error: Optional[int] = None
    duration: Optional[int] = None
    id: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    owner_id: Optional[int] = None
    waveform: Optional[List[int]] = None


class MessagesChat(PydanticModel):
    admin_id: Optional[int] = None
    id: Optional[int] = None
    kicked: Optional["BaseBoolInt"] = None
    left: Optional["BaseBoolInt"] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["MessagesChatPushSettings"] = None
    title: Optional[str] = None
    type: Optional[str] = None
    users: Optional[List[int]] = None
    is_default_photo: Optional[bool] = None


class MessagesChatFull(PydanticModel):
    admin_id: Optional[int] = None
    id: Optional[int] = None
    kicked: Optional["BaseBoolInt"] = None
    left: Optional["BaseBoolInt"] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["MessagesChatPushSettings"] = None
    title: Optional[str] = None
    type: Optional[str] = None
    users: Optional[List["MessagesUserXtrInvitedBy"]] = None


class MessagesChatPreview(PydanticModel):
    admin_id: Optional[int] = None
    joined: Optional[bool] = None
    local_id: Optional[int] = None
    members: Optional[List[int]] = None
    members_count: Optional[int] = None
    title: Optional[str] = None
    is_member: Optional[bool] = None


class MessagesChatPushSettings(PydanticModel):
    disabled_until: Optional[int] = None
    sound: Optional["BaseBoolInt"] = None


class MessagesChatRestrictions(PydanticModel):
    admins_promote_users: Optional[bool] = None
    only_admins_edit_info: Optional[bool] = None
    only_admins_edit_pin: Optional[bool] = None
    only_admins_invite: Optional[bool] = None
    only_admins_kick: Optional[bool] = None


class MessagesChatSettings(PydanticModel):
    members_count: Optional[int] = None
    friends_count: Optional[int] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    pinned_message: Optional["MessagesPinnedMessage"] = None
    state: Optional["MessagesChatSettingsState"] = None
    photo: Optional["MessagesChatSettingsPhoto"] = None
    admin_ids: Optional[List[int]] = None
    active_ids: Optional[List[int]] = None
    is_group_channel: Optional[bool] = None
    acl: Optional["MessagesChatSettingsAcl"] = None
    permissions: Optional["MessagesChatSettingsPermissions"] = None
    is_disappearing: Optional[bool] = None
    theme: Optional[str] = None
    disappearing_chat_link: Optional[str] = None
    is_service: Optional[bool] = None


class MessagesChatSettingsAcl(PydanticModel):
    can_change_info: Optional[bool] = None
    can_change_invite_link: Optional[bool] = None
    can_change_pin: Optional[bool] = None
    can_invite: Optional[bool] = None
    can_promote_users: Optional[bool] = None
    can_see_invite_link: Optional[bool] = None
    can_moderate: Optional[bool] = None
    can_copy_chat: Optional[bool] = None
    can_call: Optional[bool] = None
    can_use_mass_mentions: Optional[bool] = None
    can_change_service_type: Optional[bool] = None


class MessagesChatSettingsPermissions(PydanticModel):
    invite: Optional[str] = None
    change_info: Optional[str] = None
    change_pin: Optional[str] = None
    use_mass_mentions: Optional[str] = None
    see_invite_link: Optional[str] = None
    call: Optional[str] = None
    change_admins: Optional[str] = None


class MessagesChatSettingsPhoto(PydanticModel):
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    is_default_photo: Optional[bool] = None


class MessagesChatSettingsState(enum.Enum):
    IN = "in"
    KICKED = "kicked"
    LEFT = "left"


class MessagesConversation(PydanticModel):
    peer: Optional["MessagesConversationPeer"] = None
    sort_id: Optional["MessagesConversationSortId"] = None
    last_message_id: Optional[int] = None
    in_read: Optional[int] = None
    out_read: Optional[int] = None
    unread_count: Optional[int] = None
    is_marked_unread: Optional[bool] = None
    out_read_by: Optional["MessagesOutReadBy"] = None
    important: Optional[bool] = None
    unanswered: Optional[bool] = None
    special_service_type: Optional[str] = None
    message_request_data: Optional["MessagesMessageRequestData"] = None
    mentions: Optional[List[int]] = None
    current_keyboard: Optional["MessagesKeyboard"] = None
    push_settings: Optional["MessagesPushSettings"] = None
    can_write: Optional["MessagesConversationCanWrite"] = None
    chat_settings: Optional["MessagesChatSettings"] = None


class MessagesConversationCanWrite(PydanticModel):
    allowed: Optional[bool] = None
    reason: Optional[int] = None


class MessagesConversationMember(PydanticModel):
    can_kick: Optional[bool] = None
    invited_by: Optional[int] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_message_request: Optional[bool] = None
    join_date: Optional[int] = None
    request_date: Optional[int] = None
    member_id: Optional[int] = None


class MessagesConversationPeer(PydanticModel):
    id: Optional[int] = None
    local_id: Optional[int] = None
    type: Optional["MessagesConversationPeerType"] = None


class MessagesConversationPeerType(enum.Enum):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationSortId(PydanticModel):
    major_id: Optional[int] = None
    minor_id: Optional[int] = None


class MessagesConversationWithMessage(PydanticModel):
    conversation: Optional["MessagesConversation"] = None
    last_message: Optional["MessagesMessage"] = None


class MessagesForeignMessage(PydanticModel):
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    payload: Optional[str] = None


class MessagesForward(PydanticModel):
    owner_id: Optional[int] = None
    peer_id: Optional[int] = None
    conversation_message_ids: Optional[List[int]] = None
    message_ids: Optional[List[int]] = None
    is_reply: Optional[bool] = None


class MessagesGraffiti(PydanticModel):
    access_key: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    url: Optional[str] = None
    width: Optional[int] = None


class MessagesHistoryAttachment(PydanticModel):
    attachment: Optional["MessagesHistoryMessageAttachment"] = None
    message_id: Optional[int] = None
    from_id: Optional[int] = None
    forward_level: Optional[int] = None


class MessagesHistoryMessageAttachment(PydanticModel):
    audio: Optional["AudioAudio"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    doc: Optional["DocsDoc"] = None
    graffiti: Optional["MessagesGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["BaseLink"] = None
    photo: Optional["PhotosPhoto"] = None
    share: Optional["BaseLink"] = None
    type: Optional["MessagesHistoryMessageAttachmentType"] = None
    video: Optional["VideoVideo"] = None
    wall: Optional["BaseLink"] = None


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
    author_id: Optional[int] = None
    buttons: Optional[List[List["MessagesKeyboardButton"]]] = None
    one_time: Optional[bool] = None
    inline: Optional[bool] = None


class MessagesKeyboardButton(PydanticModel):
    action: Optional["MessagesKeyboardButtonAction"] = None
    color: Optional[str] = None


class MessagesKeyboardButtonAction(PydanticModel):
    app_id: Optional[int] = None
    hash: Optional[str] = None
    label: Optional[str] = None
    link: Optional[str] = None
    owner_id: Optional[int] = None
    payload: Optional[str] = None
    type: Optional["MessagesTemplateActionTypeNames"] = None


class MessagesLastActivity(PydanticModel):
    online: Optional["BaseBoolInt"] = None
    time: Optional[int] = None


class MessagesLongpollMessages(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class MessagesLongpollParams(PydanticModel):
    server: Optional[str] = None
    key: Optional[str] = None
    ts: Optional[int] = None
    pts: Optional[int] = None


class MessagesMessage(PydanticModel):
    action: Optional["MessagesMessageAction"] = None
    admin_author_id: Optional[int] = None
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    deleted: Optional["BaseBoolInt"] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    important: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_cropped: Optional[bool] = None
    keyboard: Optional["MessagesKeyboard"] = None
    members_count: Optional[int] = None
    out: Optional["BaseBoolInt"] = None
    payload: Optional[str] = None
    peer_id: Optional[int] = None
    random_id: Optional[int] = None
    ref: Optional[str] = None
    ref_source: Optional[str] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    pinned_at: Optional[int] = None


class MessagesMessageAction(PydanticModel):
    conversation_message_id: Optional[int] = None
    email: Optional[str] = None
    member_id: Optional[int] = None
    message: Optional[str] = None
    photo: Optional["MessagesMessageActionPhoto"] = None
    text: Optional[str] = None
    type: Optional["MessagesMessageActionStatus"] = None


class MessagesMessageActionPhoto(PydanticModel):
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None


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
    audio: Optional["AudioAudio"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    call: Optional["CallsCall"] = None
    doc: Optional["DocsDoc"] = None
    gift: Optional["GiftsLayout"] = None
    graffiti: Optional["MessagesGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_market_album: Optional["MarketMarketAlbum"] = None
    photo: Optional["PhotosPhoto"] = None
    sticker: Optional["BaseSticker"] = None
    story: Optional["StoriesStory"] = None
    type: Optional["MessagesMessageAttachmentType"] = None
    video: Optional["VideoVideo"] = None
    wall: Optional["WallWallpostFull"] = None
    wall_reply: Optional["WallWallComment"] = None
    poll: Optional["PollsPoll"] = None


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
    status: Optional[str] = None
    inviter_id: Optional[int] = None
    request_date: Optional[int] = None


class MessagesMessagesArray(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class MessagesOutReadBy(PydanticModel):
    count: Optional[int] = None
    member_ids: Optional[List[int]] = None


class MessagesPinnedMessage(PydanticModel):
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: Optional[str] = None
    keyboard: Optional["MessagesKeyboard"] = None


class MessagesPushSettings(PydanticModel):
    disabled_forever: Optional[bool] = None
    disabled_until: Optional[int] = None
    no_sound: Optional[bool] = None


class MessagesTemplateActionTypeNames(enum.Enum):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CALLBACK = "callback"


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    invited_by: Optional[int] = None


class NewsfeedCommentsFilters(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedEventActivity(PydanticModel):
    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    text: Optional[str] = None
    time: Optional[int] = None


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


class NewsfeedItemAudio(NewsfeedItemBase):
    audio: Optional["NewsfeedItemAudioAudio"] = None
    post_id: Optional[int] = None


class NewsfeedItemAudioAudio(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["AudioAudio"]] = None


class NewsfeedItemBase(PydanticModel):
    type: Optional["NewsfeedNewsfeedItemType"] = None
    source_id: Optional[int] = None
    date: Optional[int] = None


class NewsfeedItemDigest(NewsfeedItemBase):
    feed_id: Optional[str] = None
    items: Optional[List["NewsfeedItemDigestItem"]] = None
    main_post_ids: Optional[List[str]] = None
    template: Optional[str] = None
    header: Optional["NewsfeedItemDigestHeader"] = None
    footer: Optional["NewsfeedItemDigestFooter"] = None
    track_code: Optional[str] = None


class NewsfeedItemDigestButton(PydanticModel):
    title: Optional[str] = None
    style: Optional[str] = None


class NewsfeedItemDigestFooter(PydanticModel):
    style: Optional[str] = None
    text: Optional[str] = None
    button: Optional["NewsfeedItemDigestButton"] = None


class NewsfeedItemDigestFullItem(PydanticModel):
    text: Optional[str] = None
    source_name: Optional[str] = None
    attachment_index: Optional[int] = None
    attachment: Optional["WallWallpostAttachment"] = None
    style: Optional[str] = None
    post: Optional["WallWallpost"] = None


class NewsfeedItemDigestHeader(PydanticModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    style: Optional[str] = None
    button: Optional["NewsfeedItemDigestButton"] = None


NewsfeedItemDigestItem = WallWallpost


class NewsfeedItemFriend(NewsfeedItemBase):
    friends: Optional["NewsfeedItemFriendFriends"] = None


class NewsfeedItemFriendFriends(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["BaseUserId"]] = None


class NewsfeedItemHolidayRecommendationsBlockHeader(PydanticModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    image: Optional[List["BaseImage"]] = None
    action: Optional["BaseLinkButtonAction"] = None


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    photos: Optional["NewsfeedItemPhotoPhotos"] = None
    post_id: Optional[int] = None


class NewsfeedItemPhotoPhotos(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["NewsfeedNewsfeedPhoto"]] = None


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    photo_tags: Optional["NewsfeedItemPhotoTagPhotoTags"] = None
    post_id: Optional[int] = None


class NewsfeedItemPhotoTagPhotoTags(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["NewsfeedNewsfeedPhoto"]] = None


class NewsfeedItemPromoButton(NewsfeedItemBase):
    text: Optional[str] = None
    title: Optional[str] = None
    action: Optional["NewsfeedItemPromoButtonAction"] = None
    images: Optional[List["NewsfeedItemPromoButtonImage"]] = None
    track_code: Optional[str] = None


class NewsfeedItemPromoButtonAction(PydanticModel):
    url: Optional[str] = None
    type: Optional[str] = None
    target: Optional[str] = None


class NewsfeedItemPromoButtonImage(PydanticModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class NewsfeedItemTopic(NewsfeedItemBase):
    comments: Optional["BaseCommentsInfo"] = None
    likes: Optional["BaseLikesInfo"] = None
    post_id: Optional[int] = None
    text: Optional[str] = None


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    video: Optional["NewsfeedItemVideoVideo"] = None


class NewsfeedItemVideoVideo(PydanticModel):
    count: Optional[int] = None
    items: Optional[List["VideoVideo"]] = None


class NewsfeedItemWallpost(WallCarouselBase, NewsfeedItemBase):
    activity: Optional["NewsfeedEventActivity"] = None
    attachments: Optional[List["WallWallpostAttachment"]] = None
    comments: Optional["BaseCommentsInfo"] = None
    copy_history: Optional[List["WallWallpost"]] = None
    feedback: Optional["NewsfeedItemWallpostFeedback"] = None
    geo: Optional["BaseGeo"] = None
    is_favorite: Optional[bool] = None
    likes: Optional["BaseLikesInfo"] = None
    marked_as_ads: Optional["BaseBoolInt"] = None
    post_id: Optional[int] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional["NewsfeedItemWallpostType"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional["WallViews"] = None
    short_text_rate: Optional[int] = None


class NewsfeedItemWallpostFeedback(PydanticModel):
    type: Optional["NewsfeedItemWallpostFeedbackType"] = None
    question: Optional[str] = None
    answers: Optional[List["NewsfeedItemWallpostFeedbackAnswer"]] = None
    stars_count: Optional[int] = None
    gratitude: Optional[str] = None


class NewsfeedItemWallpostFeedbackAnswer(PydanticModel):
    title: Optional[str] = None
    id: Optional[str] = None


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedItemWallpostType(enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"


class NewsfeedList(PydanticModel):
    id: Optional[int] = None
    title: Optional[str] = None


class NewsfeedListFull(NewsfeedList):
    no_reposts: Optional["BaseBoolInt"] = None
    source_ids: Optional[List[int]] = None


class NewsfeedNewsfeedItem(PydanticModel):
    pass


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


class NewsfeedNewsfeedPhoto(PhotosPhoto):
    likes: Optional["BaseLikes"] = None
    comments: Optional["BaseObjectCount"] = None
    can_repost: Optional["BaseBoolInt"] = None


class NotesNote(PydanticModel):
    read_comments: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    text: Optional[str] = None
    text_wiki: Optional[str] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class NotesNoteComment(PydanticModel):
    date: Optional[int] = None
    id: Optional[int] = None
    message: Optional[str] = None
    nid: Optional[int] = None
    oid: Optional[int] = None
    reply_to: Optional[int] = None
    uid: Optional[int] = None


class NotificationsFeedback(PydanticModel):
    attachments: Optional[List["WallWallpostAttachment"]] = None
    from_id: Optional[int] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    text: Optional[str] = None
    to_id: Optional[int] = None


class NotificationsNotification(PydanticModel):
    date: Optional[int] = None
    feedback: Optional["NotificationsFeedback"] = None
    parent: Optional["NotificationsNotificationParent"] = None
    reply: Optional["NotificationsReply"] = None
    type: Optional[str] = None


class NotificationsNotificationItem(PydanticModel):
    pass


class NotificationsNotificationParent(WallWallpostToId, PhotosPhoto, BoardTopic, VideoVideo, NotificationsNotificationsComment):
    pass


class NotificationsNotificationsComment(PydanticModel):
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    post: Optional["WallWallpost"] = None
    text: Optional[str] = None
    topic: Optional["BoardTopic"] = None
    video: Optional["VideoVideo"] = None


class NotificationsReply(PydanticModel):
    date: Optional[int] = None
    id: Optional[int] = None
    text: Optional[int] = None


class NotificationsSendMessageError(PydanticModel):
    code: Optional[int] = None
    description: Optional[str] = None


class NotificationsSendMessageItem(PydanticModel):
    user_id: Optional[int] = None
    status: Optional[bool] = None
    error: Optional["NotificationsSendMessageError"] = None


class OauthError(PydanticModel):
    error: Optional[str] = None
    error_description: Optional[str] = None
    redirect_uri: Optional[str] = None


class OrdersAmount(PydanticModel):
    amounts: Optional[List["OrdersAmountItem"]] = None
    currency: Optional[str] = None


class OrdersAmountItem(PydanticModel):
    amount: Optional[int] = None
    description: Optional[str] = None
    votes: Optional[str] = None


class OrdersOrder(PydanticModel):
    amount: Optional[int] = None
    app_order_id: Optional[int] = None
    cancel_transaction_id: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    item: Optional[str] = None
    receiver_id: Optional[int] = None
    status: Optional[str] = None
    transaction_id: Optional[int] = None
    user_id: Optional[int] = None


class OrdersSubscription(PydanticModel):
    cancel_reason: Optional[str] = None
    create_time: Optional[int] = None
    id: Optional[int] = None
    item_id: Optional[str] = None
    next_bill_time: Optional[int] = None
    pending_cancel: Optional[bool] = None
    period: Optional[int] = None
    period_start_time: Optional[int] = None
    price: Optional[int] = None
    status: Optional[str] = None
    test_mode: Optional[bool] = None
    trial_expire_time: Optional[int] = None
    update_time: Optional[int] = None


class OwnerState(PydanticModel):
    state: Optional[int] = None
    description: Optional[str] = None


class PagesPrivacySettings(enum.IntEnum):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class PagesWikipage(PydanticModel):
    creator_id: Optional[int] = None
    creator_name: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    title: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PagesPrivacySettings"] = None
    who_can_view: Optional["PagesPrivacySettings"] = None


class PagesWikipageFull(PydanticModel):
    created: Optional[int] = None
    creator_id: Optional[int] = None
    current_user_can_edit: Optional["BaseBoolInt"] = None
    current_user_can_edit_access: Optional["BaseBoolInt"] = None
    edited: Optional[int] = None
    editor_id: Optional[int] = None
    group_id: Optional[int] = None
    html: Optional[str] = None
    id: Optional[int] = None
    source: Optional[str] = None
    title: Optional[str] = None
    view_url: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PagesPrivacySettings"] = None
    who_can_view: Optional["PagesPrivacySettings"] = None


class PagesWikipageHistory(PydanticModel):
    id: Optional[int] = None
    length: Optional[int] = None
    date: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None


class PhotosCommentXtrPid(PydanticModel):
    attachments: Optional[List["WallCommentAttachment"]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    pid: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    parents_stack: Optional[List[int]] = None
    thread: Optional["CommentThread"] = None


class PhotosImage(PydanticModel):
    height: Optional[int] = None
    type: Optional["PhotosImageType"] = None
    url: Optional[str] = None
    width: Optional[int] = None


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
    gid: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosMarketUploadResponse(PydanticModel):
    crop_data: Optional[str] = None
    crop_hash: Optional[str] = None
    group_id: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosMessageUploadResponse(PydanticModel):
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosOwnerUploadResponse(PydanticModel):
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosPhoto(PydanticModel):
    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["PhotosImage"]] = None
    lat: Optional[int] = None
    long: Optional[int] = None
    owner_id: Optional[int] = None
    photo_256: Optional[str] = None
    can_comment: Optional["BaseBoolInt"] = None
    place: Optional[str] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
    has_tags: Optional[bool] = None
    restrictions: Optional["MediaRestriction"] = None


class PhotosPhotoAlbum(PydanticModel):
    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    thumb: Optional["PhotosPhoto"] = None
    title: Optional[str] = None
    updated: Optional[int] = None


class PhotosPhotoAlbumFull(PydanticModel):
    can_upload: Optional["BaseBoolInt"] = None
    comments_disabled: Optional["BaseBoolInt"] = None
    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    thumb_id: Optional[int] = None
    thumb_is_last: Optional["BaseBoolInt"] = None
    thumb_src: Optional[str] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    upload_by_admins_only: Optional["BaseBoolInt"] = None


class PhotosPhotoFalseable(PydanticModel):
    pass


class PhotosPhotoFull(PydanticModel):
    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["PhotosImage"]] = None
    lat: Optional[int] = None
    likes: Optional["BaseLikes"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    comments: Optional["BaseObjectCount"] = None
    long: Optional[int] = None
    owner_id: Optional[int] = None
    post_id: Optional[int] = None
    tags: Optional["BaseObjectCount"] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoFullXtrRealOffset(PydanticModel):
    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional["BaseObjectCount"] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional["BasePropertyExists"] = None
    id: Optional[int] = None
    lat: Optional[int] = None
    likes: Optional["BaseLikes"] = None
    long: Optional[int] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    reposts: Optional["BaseObjectCount"] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    tags: Optional["BaseObjectCount"] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoSizes(PydanticModel):
    height: Optional[int] = None
    url: Optional[str] = None
    src: Optional[str] = None
    type: Optional["PhotosPhotoSizesType"] = None
    width: Optional[int] = None


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
    date: Optional[int] = None
    id: Optional[int] = None
    placer_id: Optional[int] = None
    tagged_name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
    viewed: Optional["BaseBoolInt"] = None
    x: Optional[int] = None
    x2: Optional[int] = None
    y: Optional[int] = None
    y2: Optional[int] = None


class PhotosPhotoUpload(PydanticModel):
    album_id: Optional[int] = None
    upload_url: Optional[str] = None
    fallback_upload_url: Optional[str] = None
    user_id: Optional[int] = None
    group_id: Optional[int] = None


class PhotosPhotoUploadResponse(PydanticModel):
    aid: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    photos_list: Optional[str] = None
    server: Optional[int] = None


class PhotosPhotoXtrRealOffset(PydanticModel):
    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional["BasePropertyExists"] = None
    id: Optional[int] = None
    lat: Optional[int] = None
    long: Optional[int] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoXtrTagInfo(PydanticModel):
    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    lat: Optional[int] = None
    long: Optional[int] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    placer_id: Optional[int] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    tag_created: Optional[int] = None
    tag_id: Optional[int] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosTagsSuggestionItem(PydanticModel):
    title: Optional[str] = None
    caption: Optional[str] = None
    type: Optional[str] = None
    buttons: Optional[List["PhotosTagsSuggestionItemButton"]] = None
    photo: Optional["PhotosPhoto"] = None
    tags: Optional[List["PhotosPhotoTag"]] = None
    track_code: Optional[str] = None


class PhotosTagsSuggestionItemButton(PydanticModel):
    title: Optional[str] = None
    action: Optional[str] = None
    style: Optional[str] = None


class PhotosWallUploadResponse(PydanticModel):
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PollsAnswer(PydanticModel):
    id: Optional[int] = None
    rate: Optional[int] = None
    text: Optional[str] = None
    votes: Optional[int] = None


class PollsBackground(PydanticModel):
    angle: Optional[int] = None
    color: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    images: Optional[List["BaseImage"]] = None
    points: Optional[List["BaseGradientPoint"]] = None
    type: Optional[str] = None
    width: Optional[int] = None


class PollsFriend(PydanticModel):
    id: Optional[int] = None


class PollsPoll(PydanticModel):
    anonymous: Optional["PollsPollAnonymous"] = None
    friends: Optional[List["PollsFriend"]] = None
    multiple: Optional[bool] = None
    answer_id: Optional[int] = None
    end_date: Optional[int] = None
    answer_ids: Optional[List[int]] = None
    closed: Optional[bool] = None
    is_board: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_vote: Optional[bool] = None
    can_report: Optional[bool] = None
    can_share: Optional[bool] = None
    photo: Optional["PollsBackground"] = None
    answers: Optional[List["PollsAnswer"]] = None
    created: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    author_id: Optional[int] = None
    question: Optional[str] = None
    background: Optional["PollsBackground"] = None
    votes: Optional[int] = None
    disable_unvote: Optional[bool] = None


PollsPollAnonymous = bool


class PollsVoters(PydanticModel):
    answer_id: Optional[int] = None
    users: Optional["PollsVotersUsers"] = None


class PollsVotersUsers(PydanticModel):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class PrettycardsPrettycard(PydanticModel):
    button: Optional[str] = None
    button_text: Optional[str] = None
    card_id: Optional[str] = None
    images: Optional[List["BaseImage"]] = None
    link_url: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[str] = None
    price_old: Optional[str] = None
    title: Optional[str] = None


class SearchHint(PydanticModel):
    app: Optional["AppsApp"] = None
    description: Optional[str] = None
    _global: Optional["BaseBoolInt"] = None
    group: Optional["GroupsGroup"] = None
    profile: Optional["UsersUserMin"] = None
    section: Optional["SearchHintSection"] = None
    type: Optional["SearchHintType"] = None


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
    level: Optional[int] = None
    uid: Optional[int] = None


class SecureSmsNotification(PydanticModel):
    app_id: Optional[str] = None
    date: Optional[str] = None
    id: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[str] = None


class SecureTokenChecked(PydanticModel):
    date: Optional[int] = None
    expire: Optional[int] = None
    success: Optional[int] = None
    user_id: Optional[int] = None


class SecureTransaction(PydanticModel):
    date: Optional[int] = None
    id: Optional[int] = None
    uid_from: Optional[int] = None
    uid_to: Optional[int] = None
    votes: Optional[int] = None


class StatsActivity(PydanticModel):
    comments: Optional[int] = None
    copies: Optional[int] = None
    hidden: Optional[int] = None
    likes: Optional[int] = None
    subscribed: Optional[int] = None
    unsubscribed: Optional[int] = None


class StatsCity(PydanticModel):
    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class StatsCountry(PydanticModel):
    code: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class StatsPeriod(PydanticModel):
    activity: Optional["StatsActivity"] = None
    period_from: Optional[int] = None
    period_to: Optional[int] = None
    reach: Optional["StatsReach"] = None
    visitors: Optional["StatsViews"] = None


class StatsReach(PydanticModel):
    age: Optional[List["StatsSexAge"]] = None
    cities: Optional[List["StatsCity"]] = None
    countries: Optional[List["StatsCountry"]] = None
    mobile_reach: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    sex: Optional[List["StatsSexAge"]] = None
    sex_age: Optional[List["StatsSexAge"]] = None


class StatsSexAge(PydanticModel):
    count: Optional[int] = None
    value: Optional[str] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    count_subscribers: Optional[int] = None


class StatsViews(PydanticModel):
    age: Optional[List["StatsSexAge"]] = None
    cities: Optional[List["StatsCity"]] = None
    countries: Optional[List["StatsCountry"]] = None
    mobile_views: Optional[int] = None
    sex: Optional[List["StatsSexAge"]] = None
    sex_age: Optional[List["StatsSexAge"]] = None
    views: Optional[int] = None
    visitors: Optional[int] = None


class StatsWallpostStat(PydanticModel):
    post_id: Optional[int] = None
    hide: Optional[int] = None
    join_group: Optional[int] = None
    links: Optional[int] = None
    reach_subscribers: Optional[int] = None
    reach_subscribers_count: Optional[int] = None
    reach_total: Optional[int] = None
    reach_total_count: Optional[int] = None
    reach_viral: Optional[int] = None
    reach_ads: Optional[int] = None
    report: Optional[int] = None
    to_group: Optional[int] = None
    unsubscribe: Optional[int] = None
    sex_age: Optional[List["StatsSexAge"]] = None


class StatusStatus(PydanticModel):
    text: Optional[str] = None
    audio: Optional["AudioAudio"] = None


class StorageValue(PydanticModel):
    key: Optional[str] = None
    value: Optional[str] = None


class StoreProduct(PydanticModel):
    id: Optional[int] = None
    type: Optional[str] = None
    purchased: Optional["BaseBoolInt"] = None
    active: Optional["BaseBoolInt"] = None
    promoted: Optional["BaseBoolInt"] = None
    purchase_date: Optional[int] = None
    title: Optional[str] = None
    stickers: Optional["BaseStickersList"] = None
    icon: Optional["StoreProductIcon"] = None
    previews: Optional[List["BaseImage"]] = None
    has_animation: Optional[bool] = None
    subtitle: Optional[str] = None


StoreProductIcon = List["BaseImage"]


class StoreStickersKeyword(PydanticModel):
    words: Optional[List[str]] = None
    user_stickers: Optional["StoreStickersKeywordStickers"] = None
    promoted_stickers: Optional["StoreStickersKeywordStickers"] = None
    stickers: Optional[List["StoreStickersKeywordSticker"]] = None


class StoreStickersKeywordSticker(PydanticModel):
    pack_id: Optional[int] = None
    sticker_id: Optional[int] = None


StoreStickersKeywordStickers = BaseStickersList


class StoriesClickableArea(PydanticModel):
    x: Optional[int] = None
    y: Optional[int] = None


class StoriesClickableSticker(PydanticModel):
    clickable_area: Optional[List["StoriesClickableArea"]] = None
    id: Optional[int] = None
    hashtag: Optional[str] = None
    link_object: Optional["BaseLink"] = None
    mention: Optional[str] = None
    tooltip_text: Optional[str] = None
    owner_id: Optional[int] = None
    story_id: Optional[int] = None
    question: Optional[str] = None
    question_button: Optional[str] = None
    place_id: Optional[int] = None
    market_item: Optional["MarketMarketItem"] = None
    audio: Optional["AudioAudio"] = None
    audio_start_time: Optional[int] = None
    style: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    post_owner_id: Optional[int] = None
    post_id: Optional[int] = None
    poll: Optional["PollsPoll"] = None
    color: Optional[str] = None
    sticker_id: Optional[int] = None
    sticker_pack_id: Optional[int] = None
    app: Optional["AppsAppMin"] = None
    app_context: Optional[str] = None
    has_new_interactions: Optional[bool] = None
    is_broadcast_notify_allowed: Optional[bool] = None
    situational_theme_id: Optional[int] = None
    situational_app_url: Optional[str] = None


class StoriesClickableStickers(PydanticModel):
    clickable_stickers: Optional[List["StoriesClickableSticker"]] = None
    original_height: Optional[int] = None
    original_width: Optional[int] = None


class StoriesFeedItem(PydanticModel):
    type: Optional[str] = None
    id: Optional[str] = None
    stories: Optional[List["StoriesStory"]] = None
    grouped: Optional[List["StoriesFeedItem"]] = None
    app: Optional["AppsAppMin"] = None
    promo_data: Optional["StoriesPromoBlock"] = None
    birthday_user_id: Optional[int] = None


class StoriesPromoBlock(PydanticModel):
    name: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    not_animated: Optional[bool] = None


class StoriesReplies(PydanticModel):
    count: Optional[int] = None
    new: Optional[int] = None


class StoriesStatLine(PydanticModel):
    name: Optional[str] = None
    counter: Optional[int] = None
    is_unavailable: Optional[bool] = None


class StoriesStory(PydanticModel):
    access_key: Optional[str] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_reply: Optional["BaseBoolInt"] = None
    can_see: Optional["BaseBoolInt"] = None
    can_like: Optional[bool] = None
    can_share: Optional["BaseBoolInt"] = None
    can_hide: Optional["BaseBoolInt"] = None
    date: Optional[int] = None
    expires_at: Optional[int] = None
    id: Optional[int] = None
    is_deleted: Optional[bool] = None
    is_expired: Optional[bool] = None
    link: Optional["StoriesStoryLink"] = None
    owner_id: Optional[int] = None
    parent_story: Optional["StoriesStory"] = None
    parent_story_access_key: Optional[str] = None
    parent_story_id: Optional[int] = None
    parent_story_owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    replies: Optional["StoriesReplies"] = None
    seen: Optional["BaseBoolInt"] = None
    type: Optional["StoriesStoryType"] = None
    clickable_stickers: Optional["StoriesClickableStickers"] = None
    video: Optional["VideoVideo"] = None
    views: Optional[int] = None
    can_ask: Optional["BaseBoolInt"] = None
    can_ask_anonymous: Optional["BaseBoolInt"] = None
    narratives_count: Optional[int] = None
    first_narrative_title: Optional[str] = None
    birthday_wish_user_id: Optional[int] = None
    can_use_in_narrative: Optional[bool] = None


class StoriesStoryLink(PydanticModel):
    text: Optional[str] = None
    url: Optional[str] = None


class StoriesStoryStats(PydanticModel):
    answer: Optional["StoriesStoryStatsStat"] = None
    bans: Optional["StoriesStoryStatsStat"] = None
    open_link: Optional["StoriesStoryStatsStat"] = None
    replies: Optional["StoriesStoryStatsStat"] = None
    shares: Optional["StoriesStoryStatsStat"] = None
    subscribers: Optional["StoriesStoryStatsStat"] = None
    views: Optional["StoriesStoryStatsStat"] = None
    likes: Optional["StoriesStoryStatsStat"] = None


class StoriesStoryStatsStat(PydanticModel):
    count: Optional[int] = None
    state: Optional["StoriesStoryStatsState"] = None


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
    is_liked: Optional[bool] = None
    user_id: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class UsersCareer(PydanticModel):
    city_id: Optional[int] = None
    city_name: Optional[str] = None
    company: Optional[str] = None
    country_id: Optional[int] = None
    _from: Optional[int] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    position: Optional[str] = None
    until: Optional[int] = None


class UsersExports(PydanticModel):
    facebook: Optional[int] = None
    livejournal: Optional[int] = None
    twitter: Optional[int] = None


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
    platform: Optional[int] = None
    time: Optional[int] = None


class UsersMilitary(PydanticModel):
    country_id: Optional[int] = None
    _from: Optional[int] = None
    id: Optional[int] = None
    unit: Optional[str] = None
    unit_id: Optional[int] = None
    until: Optional[int] = None


class UsersOccupation(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class UsersOnlineInfo(PydanticModel):
    visible: Optional[bool] = None
    last_seen: Optional[int] = None
    is_online: Optional[bool] = None
    app_id: Optional[int] = None
    is_mobile: Optional[bool] = None
    status: Optional[str] = None


class UsersPersonal(PydanticModel):
    alcohol: Optional[int] = None
    inspired_by: Optional[str] = None
    langs: Optional[List[str]] = None
    life_main: Optional[int] = None
    people_main: Optional[int] = None
    political: Optional[int] = None
    religion: Optional[str] = None
    religion_id: Optional[int] = None
    smoking: Optional[int] = None


class UsersRelative(PydanticModel):
    birth_date: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class UsersSchool(PydanticModel):
    city: Optional[int] = None
    _class: Optional[str] = None
    country: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[int] = None
    type_str: Optional[str] = None
    year_from: Optional[int] = None
    year_graduated: Optional[int] = None
    year_to: Optional[int] = None
    speciality: Optional[str] = None


class UsersSubscriptionsItem(PydanticModel):
    pass


class UsersUniversity(PydanticModel):
    chair: Optional[int] = None
    chair_name: Optional[str] = None
    city: Optional[int] = None
    country: Optional[int] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    university_group_id: Optional[int] = None


class UsersUser(UsersUserMin):
    sex: Optional["BaseSex"] = None
    screen_name: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    online_info: Optional["UsersOnlineInfo"] = None
    online: Optional["BaseBoolInt"] = None
    online_mobile: Optional["BaseBoolInt"] = None
    online_app: Optional[int] = None
    verified: Optional["BaseBoolInt"] = None
    trending: Optional["BaseBoolInt"] = None
    friend_status: Optional["FriendsFriendStatusStatus"] = None
    mutual: Optional["FriendsRequestsMutual"] = None


class UsersUserConnections(PydanticModel):
    skype: Optional[str] = None
    facebook: Optional[str] = None
    facebook_name: Optional[str] = None
    twitter: Optional[str] = None
    livejournal: Optional[str] = None
    instagram: Optional[str] = None


class UsersUserCounters(PydanticModel):
    albums: Optional[int] = None
    audios: Optional[int] = None
    followers: Optional[int] = None
    friends: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    notes: Optional[int] = None
    online_friends: Optional[int] = None
    pages: Optional[int] = None
    photos: Optional[int] = None
    subscriptions: Optional[int] = None
    user_photos: Optional[int] = None
    user_videos: Optional[int] = None
    videos: Optional[int] = None
    new_photo_tags: Optional[int] = None
    new_recognition_tags: Optional[int] = None
    mutual_friends: Optional[int] = None
    posts: Optional[int] = None
    articles: Optional[int] = None
    wishes: Optional[int] = None
    podcasts: Optional[int] = None
    clips: Optional[int] = None
    clips_followers: Optional[int] = None


class UsersUserFull(UsersUser):
    first_name_nom: Optional[str] = None
    first_name_gen: Optional[str] = None
    first_name_dat: Optional[str] = None
    first_name_acc: Optional[str] = None
    first_name_ins: Optional[str] = None
    first_name_abl: Optional[str] = None
    last_name_nom: Optional[str] = None
    last_name_gen: Optional[str] = None
    last_name_dat: Optional[str] = None
    last_name_acc: Optional[str] = None
    last_name_ins: Optional[str] = None
    last_name_abl: Optional[str] = None
    nickname: Optional[str] = None
    maiden_name: Optional[str] = None
    contact_name: Optional[str] = None
    domain: Optional[str] = None
    bdate: Optional[str] = None
    city: Optional["BaseCity"] = None
    country: Optional["BaseCountry"] = None
    timezone: Optional[int] = None
    owner_state: Optional["OwnerState"] = None
    photo_200: Optional[str] = None
    photo_max: Optional[str] = None
    photo_200_orig: Optional[str] = None
    photo_400_orig: Optional[str] = None
    photo_max_orig: Optional[str] = None
    photo_id: Optional[str] = None
    has_photo: Optional["BaseBoolInt"] = None
    has_mobile: Optional["BaseBoolInt"] = None
    is_friend: Optional["BaseBoolInt"] = None
    wall_comments: Optional["BaseBoolInt"] = None
    can_post: Optional["BaseBoolInt"] = None
    can_see_all_posts: Optional["BaseBoolInt"] = None
    can_see_audio: Optional["BaseBoolInt"] = None
    type: Optional["UsersUserType"] = None
    email: Optional[str] = None
    skype: Optional[str] = None
    facebook: Optional[str] = None
    facebook_name: Optional[str] = None
    twitter: Optional[str] = None
    livejournal: Optional[str] = None
    instagram: Optional[str] = None
    test: Optional["BaseBoolInt"] = None
    video_live: Optional["VideoLiveInfo"] = None
    is_video_live_notifications_blocked: Optional["BaseBoolInt"] = None
    is_service: Optional[bool] = None
    service_description: Optional[str] = None
    photo_rec: Optional["PhotosPhotoFalseable"] = None
    photo_medium: Optional["PhotosPhotoFalseable"] = None
    photo_medium_rec: Optional["PhotosPhotoFalseable"] = None
    photo: Optional[str] = None
    photo_big: Optional[str] = None
    photo_400: Optional[str] = None
    photo_max_size: Optional["PhotosPhoto"] = None
    language: Optional[str] = None
    stories_archive_count: Optional[int] = None
    wall_default: Optional[str] = None
    can_call: Optional[bool] = None
    can_see_wishes: Optional[bool] = None
    can_see_gifts: Optional["BaseBoolInt"] = None
    interests: Optional[str] = None
    books: Optional[str] = None
    tv: Optional[str] = None
    quotes: Optional[str] = None
    about: Optional[str] = None
    games: Optional[str] = None
    movies: Optional[str] = None
    activities: Optional[str] = None
    music: Optional[str] = None
    can_write_private_message: Optional["BaseBoolInt"] = None
    can_send_friend_request: Optional["BaseBoolInt"] = None
    can_be_invited_group: Optional[bool] = None
    mobile_phone: Optional[str] = None
    home_phone: Optional[str] = None
    site: Optional[str] = None
    status_audio: Optional["AudioAudio"] = None
    status: Optional[str] = None
    activity: Optional[str] = None
    last_seen: Optional["UsersLastSeen"] = None
    exports: Optional["UsersExports"] = None
    crop_photo: Optional["BaseCropPhoto"] = None
    followers_count: Optional[int] = None
    video_live_level: Optional[int] = None
    video_live_count: Optional[int] = None
    clips_count: Optional[int] = None
    blacklisted: Optional["BaseBoolInt"] = None
    blacklisted_by_me: Optional["BaseBoolInt"] = None
    is_favorite: Optional["BaseBoolInt"] = None
    is_hidden_from_feed: Optional["BaseBoolInt"] = None
    common_count: Optional[int] = None
    occupation: Optional["UsersOccupation"] = None
    career: Optional[List["UsersCareer"]] = None
    military: Optional[List["UsersMilitary"]] = None
    university: Optional[int] = None
    university_name: Optional[str] = None
    university_group_id: Optional[int] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    home_town: Optional[str] = None
    relation: Optional["UsersUserRelation"] = None
    relation_partner: Optional["UsersUserMin"] = None
    personal: Optional["UsersPersonal"] = None
    universities: Optional[List["UsersUniversity"]] = None
    schools: Optional[List["UsersSchool"]] = None
    relatives: Optional[List["UsersRelative"]] = None
    is_subscribed_podcasts: Optional[bool] = None
    can_subscribe_podcasts: Optional[bool] = None
    can_subscribe_posts: Optional[bool] = None
    counters: Optional["UsersUserCounters"] = None
    access_key: Optional[str] = None
    can_upload_doc: Optional["BaseBoolInt"] = None
    hash: Optional[str] = None
    has_email: Optional[bool] = None


class UsersUserMin(PydanticModel):
    deactivated: Optional[str] = None
    first_name: Optional[str] = None
    hidden: Optional[int] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    can_access_closed: Optional[bool] = None
    is_closed: Optional[bool] = None


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
    connections: Optional["UsersUserConnections"] = None
    bdate: Optional[str] = None
    bdate_visibility: Optional[int] = None
    city: Optional["BaseCity"] = None
    country: Optional["BaseCountry"] = None
    first_name: Optional[str] = None
    home_town: Optional[str] = None
    last_name: Optional[str] = None
    maiden_name: Optional[str] = None
    name_request: Optional["AccountNameRequest"] = None
    personal: Optional["UsersPersonal"] = None
    phone: Optional[str] = None
    relation: Optional["UsersUserRelation"] = None
    relation_partner: Optional["UsersUserMin"] = None
    relation_pending: Optional["BaseBoolInt"] = None
    relation_requests: Optional[List["UsersUserMin"]] = None
    screen_name: Optional[str] = None
    sex: Optional["BaseSex"] = None
    status: Optional[str] = None
    status_audio: Optional["AudioAudio"] = None
    interests: Optional["AccountUserSettingsInterests"] = None
    languages: Optional[List[str]] = None


class UsersUserType(enum.Enum):
    PROFILE = "profile"


class UsersUserXtrCounters(UsersUserFull):
    pass


class UsersUserXtrType(UsersUser):
    type: Optional["UsersUserType"] = None


class UsersUsersArray(PydanticModel):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class UtilsDomainResolved(PydanticModel):
    object_id: Optional[int] = None
    group_id: Optional[int] = None
    type: Optional["UtilsDomainResolvedType"] = None


class UtilsDomainResolvedType(enum.Enum):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(PydanticModel):
    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    timestamp: Optional[int] = None
    url: Optional[str] = None
    views: Optional[int] = None


class UtilsLinkChecked(PydanticModel):
    link: Optional[str] = None
    status: Optional["UtilsLinkCheckedStatus"] = None


class UtilsLinkCheckedStatus(enum.Enum):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(PydanticModel):
    key: Optional[str] = None
    stats: Optional[List["UtilsStats"]] = None


class UtilsLinkStatsExtended(PydanticModel):
    key: Optional[str] = None
    stats: Optional[List["UtilsStatsExtended"]] = None


class UtilsShortLink(PydanticModel):
    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    url: Optional[str] = None


class UtilsStats(PydanticModel):
    timestamp: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsCity(PydanticModel):
    city_id: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsCountry(PydanticModel):
    country_id: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsExtended(PydanticModel):
    cities: Optional[List["UtilsStatsCity"]] = None
    countries: Optional[List["UtilsStatsCountry"]] = None
    sex_age: Optional[List["UtilsStatsSexAge"]] = None
    timestamp: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsSexAge(PydanticModel):
    age_range: Optional[str] = None
    female: Optional[int] = None
    male: Optional[int] = None


class VideoLiveInfo(PydanticModel):
    enabled: Optional["BaseBoolInt"] = None
    is_notifications_blocked: Optional["BaseBoolInt"] = None


class VideoLiveSettings(PydanticModel):
    can_rewind: Optional["BaseBoolInt"] = None
    is_endless: Optional["BaseBoolInt"] = None
    max_duration: Optional[int] = None


class VideoRestrictionButton(PydanticModel):
    action: Optional[str] = None
    title: Optional[str] = None


class VideoSaveResult(PydanticModel):
    access_key: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    upload_url: Optional[str] = None
    video_id: Optional[int] = None


class VideoVideo(PydanticModel):
    access_key: Optional[str] = None
    adding_date: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_edit: Optional["BaseBoolInt"] = None
    can_like: Optional["BaseBoolInt"] = None
    can_repost: Optional["BaseBoolInt"] = None
    can_subscribe: Optional["BaseBoolInt"] = None
    can_add_to_faves: Optional["BaseBoolInt"] = None
    can_add: Optional["BaseBoolInt"] = None
    can_attach_link: Optional["BaseBoolInt"] = None
    is_private: Optional["BaseBoolInt"] = None
    comments: Optional[int] = None
    date: Optional[int] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    image: Optional[List["VideoVideoImage"]] = None
    first_frame: Optional[List["VideoVideoImage"]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    title: Optional[str] = None
    is_favorite: Optional[bool] = None
    player: Optional[str] = None
    processing: Optional["BasePropertyExists"] = None
    converting: Optional["BaseBoolInt"] = None
    restriction: Optional["MediaRestriction"] = None
    added: Optional["BaseBoolInt"] = None
    is_subscribed: Optional["BaseBoolInt"] = None
    track_code: Optional[str] = None
    repeat: Optional["BasePropertyExists"] = None
    type: Optional[str] = None
    views: Optional[int] = None
    local_views: Optional[int] = None
    content_restricted: Optional[int] = None
    content_restricted_message: Optional[str] = None
    balance: Optional[int] = None
    live_status: Optional[str] = None
    live: Optional["BasePropertyExists"] = None
    upcoming: Optional["BasePropertyExists"] = None
    live_start_time: Optional[int] = None
    live_notify: Optional["BaseBoolInt"] = None
    spectators: Optional[int] = None
    platform: Optional[str] = None
    likes: Optional["BaseLikes"] = None
    reposts: Optional["BaseRepostsInfo"] = None


class VideoVideoAlbumFull(PydanticModel):
    count: Optional[int] = None
    id: Optional[int] = None
    image: Optional[List["VideoVideoImage"]] = None
    image_blur: Optional["BasePropertyExists"] = None
    is_system: Optional["BasePropertyExists"] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class VideoVideoFiles(PydanticModel):
    external: Optional[str] = None
    mp4_240: Optional[str] = None
    mp4_360: Optional[str] = None
    mp4_480: Optional[str] = None
    mp4_720: Optional[str] = None
    mp4_1080: Optional[str] = None
    flv_320: Optional[str] = None


class VideoVideoFull(VideoVideo):
    files: Optional["VideoVideoFiles"] = None
    live_settings: Optional["VideoLiveSettings"] = None


class VideoVideoImage(BaseImage):
    with_padding: Optional["BasePropertyExists"] = None


class WallAppPost(PydanticModel):
    id: Optional[int] = None
    name: Optional[str] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class WallAttachedNote(PydanticModel):
    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    read_comments: Optional[int] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class WallCarouselBase(PydanticModel):
    carousel_offset: Optional[int] = None


class WallCommentAttachment(PydanticModel):
    audio: Optional["AudioAudio"] = None
    doc: Optional["DocsDoc"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_market_album: Optional["MarketMarketAlbum"] = None
    note: Optional["WallAttachedNote"] = None
    page: Optional["PagesWikipageFull"] = None
    photo: Optional["PhotosPhoto"] = None
    sticker: Optional["BaseSticker"] = None
    type: Optional["WallCommentAttachmentType"] = None
    video: Optional["VideoVideo"] = None


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
    coordinates: Optional[str] = None
    place: Optional["BasePlace"] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class WallGraffiti(PydanticModel):
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_200: Optional[str] = None
    photo_586: Optional[str] = None


class WallPostCopyright(PydanticModel):
    id: Optional[int] = None
    link: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class WallPostSource(PydanticModel):
    data: Optional[str] = None
    platform: Optional[str] = None
    type: Optional["WallPostSourceType"] = None
    url: Optional[str] = None


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
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class WallViews(PydanticModel):
    count: Optional[int] = None


class WallWallComment(PydanticModel):
    attachments: Optional[List["WallCommentAttachment"]] = None
    date: Optional[int] = None
    donut: Optional["WallWallCommentDonut"] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    real_offset: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    thread: Optional["CommentThread"] = None
    post_id: Optional[int] = None
    owner_id: Optional[int] = None
    parents_stack: Optional[List[int]] = None
    deleted: Optional[bool] = None


class WallWallCommentDonut(PydanticModel):
    is_don: Optional[bool] = None
    placeholder: Optional["WallWallCommentDonutPlaceholder"] = None


class WallWallCommentDonutPlaceholder(PydanticModel):
    text: Optional[str] = None


class WallWallpost(PydanticModel):
    access_key: Optional[str] = None
    attachments: Optional[List["WallWallpostAttachment"]] = None
    copyright: Optional["WallPostCopyright"] = None
    date: Optional[int] = None
    edited: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["WallGeo"] = None
    id: Optional[int] = None
    is_archived: Optional[bool] = None
    is_favorite: Optional[bool] = None
    likes: Optional["BaseLikesInfo"] = None
    owner_id: Optional[int] = None
    poster: Optional[dict] = None
    post_id: Optional[int] = None
    parents_stack: Optional[List[int]] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional["WallPostType"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional["WallViews"] = None


class WallWallpostAttachment(PydanticModel):
    access_key: Optional[str] = None
    album: Optional["PhotosPhotoAlbum"] = None
    app: Optional["WallAppPost"] = None
    audio: Optional["AudioAudio"] = None
    doc: Optional["DocsDoc"] = None
    event: Optional["EventsEventAttach"] = None
    group: Optional["GroupsGroupAttach"] = None
    graffiti: Optional["WallGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_album: Optional["MarketMarketAlbum"] = None
    note: Optional["WallAttachedNote"] = None
    page: Optional["PagesWikipageFull"] = None
    photo: Optional["PhotosPhoto"] = None
    photos_list: Optional[List[str]] = None
    poll: Optional["PollsPoll"] = None
    posted_photo: Optional["WallPostedPhoto"] = None
    type: Optional["WallWallpostAttachmentType"] = None
    video: Optional["VideoVideo"] = None


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
    placeholder: Optional["WallWallpostCommentsDonutPlaceholder"] = None


class WallWallpostCommentsDonutPlaceholder(PydanticModel):
    text: Optional[str] = None


class WallWallpostDonut(PydanticModel):
    is_donut: Optional[bool] = None
    paid_duration: Optional[int] = None
    placeholder: Optional["WallWallpostDonutPlaceholder"] = None
    can_publish_free_copy: Optional[bool] = None
    edit_mode: Optional[str] = None


class WallWallpostDonutPlaceholder(PydanticModel):
    text: Optional[str] = None


class WallWallpostFull(WallCarouselBase, WallWallpost):
    copy_history: Optional[List["WallWallpost"]] = None
    can_edit: Optional["BaseBoolInt"] = None
    created_by: Optional[int] = None
    can_delete: Optional["BaseBoolInt"] = None
    can_pin: Optional["BaseBoolInt"] = None
    donut: Optional["WallWallpostDonut"] = None
    is_pinned: Optional[int] = None
    comments: Optional["BaseCommentsInfo"] = None
    marked_as_ads: Optional["BaseBoolInt"] = None
    short_text_rate: Optional[int] = None


class WallWallpostToId(PydanticModel):
    attachments: Optional[List["WallWallpostAttachment"]] = None
    comments: Optional["BaseCommentsInfo"] = None
    copy_owner_id: Optional[int] = None
    copy_post_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["WallGeo"] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    likes: Optional["BaseLikesInfo"] = None
    post_id: Optional[int] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional["WallPostType"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    to_id: Optional[int] = None


class WidgetsCommentMedia(PydanticModel):
    item_id: Optional[int] = None
    owner_id: Optional[int] = None
    thumb_src: Optional[str] = None
    type: Optional["WidgetsCommentMediaType"] = None


class WidgetsCommentMediaType(enum.Enum):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(PydanticModel):
    can_post: Optional["BaseBoolInt"] = None
    count: Optional[int] = None
    replies: Optional[List["WidgetsCommentRepliesItem"]] = None


class WidgetsCommentRepliesItem(PydanticModel):
    cid: Optional[int] = None
    date: Optional[int] = None
    likes: Optional["WidgetsWidgetLikes"] = None
    text: Optional[str] = None
    uid: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class WidgetsWidgetComment(PydanticModel):
    attachments: Optional[List["WallCommentAttachment"]] = None
    can_delete: Optional["BaseBoolInt"] = None
    comments: Optional["WidgetsCommentReplies"] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    media: Optional["WidgetsCommentMedia"] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional[int] = None
    reposts: Optional["BaseRepostsInfo"] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class WidgetsWidgetLikes(PydanticModel):
    count: Optional[int] = None


class WidgetsWidgetPage(PydanticModel):
    comments: Optional["BaseObjectCount"] = None
    date: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    likes: Optional["BaseObjectCount"] = None
    page_id: Optional[str] = None
    photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None


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