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
    templateFeed = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')
    templateContent = jsonLoad(pFile = f'{gDirectory}/backend/template/content.json')

    # >

    # set (rData) <
    rData = templateFeed
    rData['feed']['link'] = pLinkInput
    rData['feed']['image'] = pImageInput
    rData['feed']['border'] = pBorderInput

    # >

    # try if (content and subject) <
    # except then (only content) <
    try:

        content = list(pData['content'].keys())
        subject = pData['content'][pContentLoad]['subject']

    except: subject = None

    # >

    # if (independent content) <
    # if (independent subject) <
    # if (dependent content) <
    # if (dependent subject) <
    if (pContentCreate and (not pContentLoad)): contentIndex = 0
    if (subject and pSubjectCreate and (not pSubjectLoad)): subjectIndex = 0
    if (pContentCreate and pContentLoad): contentIndex = content.index(pContentLoad)
    if (subject and pSubjectCreate and pSubjectLoad): subjectIndex = subject.index(pSubjectLoad)

    # >

    #

    return rData













