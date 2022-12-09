# import <


# >


def insertFunction(

        pData: dict,

        pContentLoad: str,
        pSubjectLoad: str,
        pContentCreate: str,
        pSubjectCreate: str,

        pLinkInput: str,
        pImageInput: str,
        pBorderInput: str,
        pContentInput: str,
        pTextColorInput: str,
        pTitleColorInput: str,
        pBackgroundInput: str

):
    '''  '''

    # local <
    content = None
    subject = None
    whichContent = pContentCreate if (pContentCreate) else pContentLoad
    templateFeed = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')
    templateContent = jsonLoad(pFile = f'{gDirectory}/backend/template/content.json')

    # >

    # set (rData) <
    rData = templateFeed
    rData['feed']['link'] = pLinkInput
    rData['feed']['image'] = pImageInput
    rData['feed']['border'] = pBorderInput

    # >

    # if (content) <
    # if (insertion) <
    # elif (new) <
    if (pContentLoad): content = list(pData['content'].keys())
    if (pContentLoad and pContentCreate): content.insert(

        content.index(pContentLoad),
        pContentCreate

    )
    elif (pContentCreate and (not pContentLoad)): content = [pContentCreate]

    # >

    # if (subject) <
    # if (insertion) <
    # elif (new) <
    # elif (existing) <
    if (pSubjectLoad): subject = pData['content'][pContentLoad]['subject']
    if (pSubjectLoad and pSubjectCreate): subject.insert(

        pSubjectLoad,
        [

            pSubjectCreate,
            pTextColorInput,
            pContentInput

        ]

    )
    elif (pSubjectCreate and (not pSubjectLoad)): subject = [pSubjectCreate]
    elif (pSubjectLoad and (not pSubjectCreate)):

        subject[pSubjectLoad] = [

            pSubjectLoad,
            pTextColorInput,
            pContentInput

        ]

    # >

    # iterate (content) <
    for i, c in enumerate(content):

        # if (match) <
        # elif (not match) <
        # else then (no subject) <
        if (subject and (c == whichContent)):

            pass

        elif (subject and (c != whichContent)):

            pass

        else: pass

        # >

    # >
