###### Developed by Sunghyun Cho on August 20th, 2018.
# CafeteriaFairy.py
### 급식요정.py
-----
### [이 문서를 한글로 읽기](https://github.com/anaclumos/CafeteriaFairy/blob/master/README%20in%20Korean.md)

## Feature
Extracts cafeteria food information from a website of Ministry of Education, Republic of Korea, and creates JSON database with it.

## Usage
Planned to be added in [kakaominsa](https://github.com/anaclumos/kakaominsa)

## Strength
|Strength|Explanation|
|---|---|
|Richer data|Can get menu info, allergic info, food source info, and nutrition info.|
|Adaptiveness|It can adaptively parse the MoE web, eventhough the MoE modifies the web structure.|
|High code reusability|Every function is moduled, therefore can be reused anytime.|
|Resource efficient|It only executes when the JSON database does not have the requested data.|


## Example database result

```
{
    "2018.08.19(일)": {
        "메뉴 정보": [
            "짜장밥2.5.6.10.",
            "계란파국1.9.",
            "배추김치9.13.",
            "씨리얼+우유+토스트+주스+김1.2.4.5.6.12.13.",
            "생과일",
            "군만두1.2.5.6.10.13.",
            "오이양파무침"
        ],
        "인원 정보": "435명",
        "영양 정보": {
            "에너지(kcal)": "837.5",
            "탄수화물(g)": "137",
            "단백질(g)": "24.2",
            "지방(g)": "20.5",
            "비타민A(R.E)": "303.7",
            "티아민(mg)": "0.7",
            "리보플라빈(mg)": "1.6",
            "비타민C(mg)": "82.2",
            "칼슘(mg)": "225.8",
            "철분(mg)": "5.1"
        },
        "원산지 정보": {
            "쌀": "국내산",
            "김치류": "국내산",
            "고춧가루(김치류)": "국내산",
            "쇠고기(종류)": "국내산(한우)",
            "돼지고기": "국내산",
            "닭고기": "국내산",
            "오리고기": "국내산",
            "양고기": "국내산",
            "쇠고기 식육가공품": "국내산",
            "돼지고기 식육가공품": "국내산",
            "닭고기 식육가공품": "국내산",
            "오리고기 가공품": "국내산",
            "양고기 식육가공품": "국내산",
            "넙치": "국내산",
            "조피볼락": "국내산",
            "참돔": "국내산",
            "미꾸라지": "국내산",
            "뱀장어": "국내산",
            "낙지": "국내산",
            "명태": "국내산",
            "고등어": "국내산",
            "갈치": "국내산",
            "오징어": "국내산",
            "꽃게": "국내산",
            "참조기": "국내산",
            "넙치 수산가공품": "",
            "조피볼락 수산가공품": "",
            "참돔 수산가공품": "",
            "미꾸라지 수산가공품": "",
            "뱀장어 수산가공품": "",
            "낙지 수산가공품": "",
            "명태 수산가공품": "",
            "고등어 수산가공품": "",
            "갈치 수산가공품": "",
            "오징어 수산가공품": "",
            "꽃게 수산가공품": "",
            "참조기 수산가공품": "",
            "두부": "국내산",
            "콩": "국내산"
        },
        "비고": ""
    },
(이하 생략)
```