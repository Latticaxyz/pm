from __future__ import annotations

from typing import Required, TypeAlias, TypedDict


class MarketRes(TypedDict, total=False):
    id: Required[str]
    question: str
    conditionId: Required[str]
    slug: str
    twitterCardImage: str
    resolutionSource: str
    endDate: str
    category: str
    ammType: str
    liquidity: str
    sponsorName: str
    sponsorImage: str
    startDate: str
    xAxisValue: str
    yAxisValue: str
    denominationToken: str
    fee: str
    image: str
    icon: str
    lowerBound: str
    upperBound: str
    description: str
    outcomes: str
    outcomePrices: str
    volume: str
    active: bool
    marketType: str
    formatType: str
    lowerBoundDate: str
    upperBoundDate: str
    closed: bool
    marketMakerAddress: Required[str]
    createdBy: int
    updatedBy: int
    createdAt: str
    updatedAt: str
    closedTime: str
    wideFormat: bool
    new: bool
    mailchimpTag: str
    featured: bool
    # from actual response
    submitted_by: str
    archived: bool
    resolvedBy: str
    restricted: bool
    marketGroup: int
    groupItemTitle: str
    groupItemThreshold: str
    questionID: str
    umaEndDate: str
    enableOrderBook: bool
    orderPriceMinTickSize: float
    orderMinSize: float
    umaResolutionStatus: str
    curationOrder: int
    volumeNum: float
    liquidityNum: float
    endDateIso: str
    startDateIso: str
    umaEndDateIso: str
    hasReviewedDates: bool
    readyForCron: bool
    commentsEnabled: bool
    volume24hr: float
    volume1wk: float
    volume1mo: float
    volume1yr: float
    gameStartTime: str
    secondsDelay: int
    clobTokenIds: str
    disqusThread: str
    shortOutcomes: str
    teamAID: str
    teamBID: str
    umaBond: str
    umaReward: str
    fpmmLive: bool
    volume24hrAmm: float
    volume1wkAmm: float
    volume1moAmm: float
    volume1yrAmm: float
    volume24hrClob: float
    volume1wkClob: float
    volume1moClob: float
    volume1yrClob: float
    volumeAmm: float
    volumeClob: float
    liquidityAmm: float
    liquidityClob: float
    makerBaseFee: int
    takerBaseFee: int
    customLiveness: int
    acceptingOrders: bool
    negRisk: bool
    negRiskMarketID: str
    negRiskRequestID: str
    notificationsEnabled: bool
    score: int
    imageOptimized: ImageOptimizedRes
    iconOptimized: IconOptimizedRes
    events: EventsRes
    categories: CategoriesRes
    tags: TagsRes
    creator: str
    ready: bool
    funded: bool
    pastSlugs: str
    readyTimestamp: str
    fundedTimestamp: str
    acceptingOrdersTimestamp: str
    competitive: float
    pagerDutyNotificationEnabled: bool
    approved: bool
    clobRewards: list[ClobRewardsRes]
    rewardsMinSize: float
    rewardsMaxSpread: float
    spread: float
    automaticallyResolved: bool
    oneDayPriceChange: float
    oneHourPriceChange: float
    oneWeekPriceChange: float
    oneMonthPriceChange: float
    oneYearPriceChange: float
    lastTradePrice: float
    bestBid: float
    bestAsk: float
    automaticallyActive: bool
    clearBookOnStart: bool
    chartColor: str
    seriesColor: str
    showGmpSeries: bool
    showGmpOutcome: bool
    manualActivation: bool
    negRiskOther: bool
    gameId: str
    groupItemRange: str
    sportsMarketType: str
    line: float
    umaResolutionStatuses: str
    pendingDeployment: bool
    deploying: bool
    deployingTimestamp: str
    scheduledDeploymentTimestamp: str
    rfqEnabled: bool
    holdingRewardsEnabled: bool
    feesEnabled: bool
    eventStartTime: str


MarketsRes: TypeAlias = list[MarketRes]


class ImageOptimizedRes(TypedDict, total=False):
    id: Required[str]
    imageUrlSource: str
    imageUrlOptimized: str
    imageSizeKbSource: float
    imageSizeKbOptimized: float
    imageOptimizedComplete: bool
    imageOptimizedLastUpdated: str
    relID: int
    field: str
    relname: str


class IconOptimizedRes(TypedDict, total=False):
    id: Required[str]
    imageUrlSource: str
    imageUrlOptimized: str
    imageSizeKbSource: float
    imageSizeKbOptimized: float
    imageOptimizedComplete: bool
    imageOptimizedLastUpdated: str
    relID: int
    field: str
    relname: str


FeaturedImageOptimizedRes: TypeAlias = ImageOptimizedRes

HeaderImageOptimizedRes: TypeAlias = ImageOptimizedRes

ProfileImageOptimizedRes: TypeAlias = ImageOptimizedRes


class ClobRewardsRes(TypedDict, total=False):
    id: Required[str]
    conditionId: str
    assetAddress: str
    rewardsAmount: int
    rewardsDailyRate: int
    startDate: str
    endDate: str


class CategoryRes(TypedDict, total=False):
    id: Required[str]
    label: str
    parentCategory: str
    slug: str
    publishedAt: str
    createdBy: str
    updatedBy: str
    createdAt: str
    updatedAt: str


CategoriesRes: TypeAlias = list[CategoryRes]


class EventRes(TypedDict, total=False):
    id: Required[str]
    ticker: str
    slug: str
    title: str
    subtitle: str
    description: str
    resolutionSource: str
    startDate: str
    creationDate: str
    endDate: str
    image: str
    icon: str
    active: bool
    closed: bool
    archived: bool
    new: bool
    featured: bool
    restricted: bool
    liquidity: float
    volume: float
    openInterest: float
    sortBy: str
    category: str
    subcategory: str
    isTemplate: bool
    templateVariables: str
    published_at: str
    createdBy: str
    updatedBy: str
    createdAt: str
    updatedAt: str
    commentsEnabled: bool
    competitive: float
    volume24hr: float
    volume1wk: float
    volume1mo: float
    volume1yr: float
    featuredImage: str
    disqusThread: str
    parentEvent: str
    enableOrderBook: bool
    liquidityAmm: float
    liquidityClob: float
    negRisk: bool
    negRiskMarketID: str
    negRiskFeeBips: int
    commentCount: int
    imageOptimized: ImageOptimizedRes
    iconOptimized: IconOptimizedRes
    featuredImageOptimized: FeaturedImageOptimizedRes
    subEvents: list[str]
    markets: MarketsRes
    series: SeriesRes
    categories: CategoriesRes
    collections: CollectionsRes
    tags: TagsRes
    cyom: bool
    closedTime: str
    showAllOutcomes: bool
    showMarketImages: bool
    automaticallyResolved: bool
    enableNegRisk: bool
    automaticallyActive: bool
    eventDate: str
    startTime: str
    eventWeek: int
    seriesSlug: str
    score: str
    elapsed: str
    period: str
    live: bool
    ended: bool
    finishedTimestamp: str
    gmpChartMode: str
    negRiskAugmented: bool
    countryName: str
    electionType: str
    eventCreators: list[EventCreatorRes]
    tweetCount: int
    chats: ChatsRes
    featuredOrder: int
    estimateValue: bool
    cantEstimate: bool
    estimatedValue: str
    templates: TemplatesRes
    spreadsMainLine: float
    totalsMainLine: float
    carouselMap: str
    pendingDeployment: bool
    deploying: bool
    deployingTimestamp: str
    scheduledDeploymentTimestamp: str
    gameStatus: str
    requiresTranslation: bool


EventsRes: TypeAlias = list[EventRes]


class EventCreatorRes(TypedDict, total=False):
    id: Required[str]
    creatorName: str
    creatorHandle: str
    creatorUrl: str
    creatorImage: str
    createdAt: str
    updatedAt: str


class TemplateRes(TypedDict, total=False):
    id: Required[str]
    eventTitle: str
    eventSlug: str
    eventImage: str
    marketTitle: str
    description: str
    resolutionSource: str
    negRisk: bool
    sortBy: str
    showMarketImages: bool
    seriesSlug: str
    outcomes: str


TemplatesRes: TypeAlias = list[TemplateRes]


class CollectionRes(TypedDict, total=False):
    id: Required[str]
    ticker: str
    slug: str
    title: str
    subtitle: str
    collectionType: str
    description: str
    tags: str
    image: str
    icon: str
    headerImage: str
    layout: str
    active: bool
    closed: bool
    archived: bool
    new: bool
    featured: bool
    restricted: bool
    templateVariables: str
    publishedAt: str
    createdBy: str
    updatedBy: str
    createdAt: str
    updatedAt: str
    commentsEnabled: bool
    imageOptimized: list[ImageOptimizedRes]
    iconOptimized: list[IconOptimizedRes]
    headerImageOptimized: list[HeaderImageOptimizedRes]


CollectionsRes: TypeAlias = list[CollectionRes]


class TagRes(TypedDict):
    id: str
    label: str
    slug: str
    forceShow: bool
    publishedAt: str
    updatedBy: int
    createdAt: str
    updatedAt: str
    forceHide: bool
    requiresTranslation: bool


TagsRes: TypeAlias = list[TagRes]


class RelatedTagRes(TypedDict):
    id: str
    tagId: int
    relatedTagId: int
    rank: int


RelatedTagsRes: TypeAlias = list[RelatedTagRes]


class SingleSeriesRes(TypedDict, total=False):
    id: Required[str]
    ticker: str
    slug: str
    title: str
    subtitle: str
    seriesType: str
    recurrence: str
    description: str
    image: str
    icon: str
    layout: str
    active: bool
    closed: bool
    archived: bool
    new: bool
    featured: bool
    restricted: bool
    isTemplate: bool
    templateVariables: bool
    publishedAt: str
    createdBy: str
    updatedBy: str
    createdAt: str
    updatedAt: str
    commentsEnabled: bool
    competitive: str
    volume24hr: float
    volume: float
    liquidity: float
    startDate: str
    pythTokenID: str
    cgAssetName: str
    score: int
    events: EventsRes
    collections: CollectionsRes
    categories: CategoriesRes
    tags: TagsRes
    commentCount: int
    chats: ChatsRes
    requiresTranslation: bool


SeriesRes: TypeAlias = list[SingleSeriesRes]


class ProfileRes(TypedDict, total=False):
    createdAt: str
    proxyWallet: str
    baseAddress: str
    profileImage: str
    displayUsernamePublic: bool
    bio: str
    pseudonym: str
    name: str
    users: list[UsersRes]
    xUsername: str
    verifiedBadge: bool
    # docs claim
    positions: list[ProfilePositionRes]
    profileImageOptimized: ProfileImageOptimizedRes


ProfilesRes: TypeAlias = list[ProfileRes]


class ProfilePositionRes(TypedDict, total=False):
    tokenId: str
    positionSize: str


class UsersRes(TypedDict):
    id: str
    creator: bool
    mod: bool


class ChatRes(TypedDict, total=False):
    id: Required[str]
    channelId: str
    channelName: str
    channelImage: str
    live: bool
    startTime: str
    endTime: str


ChatsRes: TypeAlias = list[ChatRes]


class CommentRes(TypedDict, total=False):
    id: Required[str]
    body: str
    parentEntityType: str
    parentEntityID: int
    parentCommentID: str
    userAddress: str
    replyAddress: str
    createdAt: str
    updatedAt: str
    profile: ProfileRes
    reactions: ReactionsRes
    reportCount: int
    reactionCount: int


CommentsRes: TypeAlias = list[CommentRes]


class ReactionRes(TypedDict, total=False):
    id: Required[str]
    commentID: int
    reactionType: str
    icon: str
    userAddress: str
    createdAt: str
    profile: ProfileRes


ReactionsRes: TypeAlias = list[ReactionRes]
