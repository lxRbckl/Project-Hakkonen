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
    if (pContentLoad or pContentCreate): content = list(pData['content'].keys())
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
    if (pSubjectLoad or pSubjectCreate): subject = pData['content'][pContentLoad]['subject']
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

    # try if (content and subject) <
    # except then (only content) <
    try:

        pass

    except: pass

    # >
