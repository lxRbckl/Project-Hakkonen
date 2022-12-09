# import <
from lxRbckl import jsonLoad

from backend.resource import gDirectory

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
    rData = jsonLoad(pFile = f'{gDirectory}/backend/template/feed.json')
    templateContent = jsonLoad(pFile = f'{gDirectory}/backend/template/content.json')

    # >

    # if (content) <
    # if (new) <
    # if (insertion) <
    if (pContentLoad): content = list(pData['content'].keys())
    if (pContentCreate and (not pContentLoad)): content = [pContentCreate]
    if (pContentLoad and pContentCreate): content.insert(

        content.index(pContentLoad),
        pContentCreate

    )

    # >

    # if (subject) <
    # if (new) <
    # if (insertion) <
    # elif (existing) <
    if (pSubjectLoad): subject = pData['content'][pContentLoad]['subject']
    if (pSubjectCreate and (not pSubjectLoad)): subject = [pSubjectCreate]
    if (pSubjectLoad and pSubjectCreate): subject.insert(

        int(pSubjectLoad),
        [

            pSubjectCreate,
            pTextColorInput,
            pContentInput.split('\n\n') if (pSubjectCreate in ['text']) else pContentInput

        ]

    )
    if (pSubjectLoad and (not pSubjectCreate)):

        subject[int(pSubjectLoad)] = [

            pData['content'][pContentLoad]['subject'][int(pSubjectLoad)][0],
            pTextColorInput,
            pContentInput

        ]

    # >

    # set (link, image, border) <
    # iterate (content) <
    rData['feed']['link'] = pLinkInput
    rData['feed']['image'] = pImageInput
    rData['feed']['border'] = pBorderInput
    for i, c in enumerate(content):

        # if (match) <
        # elif (not match) <
        # else then (no subject) <
        if (subject): subject = pData['content'][c]['subject']
        if (subject and (c == whichContent)):

            rData['feed']['content'][c] = {

                'title' : pTitleColorInput,
                'background' : pBackgroundInput,
                'subject' : [s for s in subject] if (subject) else pData

            }

        elif (subject and (c != whichContent)): rData['feed']['content'][c] = pData['content'][c]
        else: rData['feed']['content'][c] = templateContent

        # >

    # >

    return rData
