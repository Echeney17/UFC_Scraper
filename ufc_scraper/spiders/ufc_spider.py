import scrapy
from scrapy import Request




class UfcSpiderSpider(scrapy.Spider):
    name = 'ufc_spider'
    allowed_domains = ['www.ufcstats.com']
    # start_urls = ['http://www.ufcstats.com/statistics/events/completed/']

    def start_requests(self):
        yield Request(url="http://www.ufcstats.com/statistics/events/completed?page=all", callback=self.parse_events, dont_filter=True)


    def parse_events(self, response):
        event_urls=response.xpath("//i[@class='b-statistics__table-content']/a[@class='b-link b-link_style_black']/@href").extract()
        for links in event_urls:
            yield Request(url=links, callback=self.parse_results, dont_filter=True)

    def parse_results(self, response):
        fight_details=response.xpath("//p[@class='b-fight-details__table-text']/a[@class='b-flag b-flag_style_green']/@href").extract()
        for links in fight_details:
            yield Request(url=links, callback=self.parse_details, dont_filter=True)
            
    def parse_details(self, response):
        fight_title=response.xpath("normalize-space(/html/body/section/div/h2/a/text())").extract_first()
        loser=response.xpath("//i[@class='b-fight-details__person-status b-fight-details__person-status_style_gray']/following-sibling::div/h3/a/text()").extract_first()
        winner=response.xpath("//i[@class='b-fight-details__person-status b-fight-details__person-status_style_green']/following-sibling::div/h3/a/text()").extract_first()
        weight_class=response.xpath("normalize-space((//div[@class='b-fight-details__fight-head']/i/text())[2])").extract_first()
        if weight_class:
            pass
        else:
            weight_class=response.xpath("normalize-space((//div[@class='b-fight-details__fight-head']/i/text())[1])").extract_first()
        method=response.xpath("//i[@class='b-fight-details__label'][contains(text(), 'Method')]/following-sibling::i/text()").extract_first()
        rnds=response.xpath("normalize-space((/html/body/section/div/div/div[2]/div[2]/p[1]/i[2]/text())[2])").extract_first()
        time=response.xpath("normalize-space((/html/body/section/div/div/div[2]/div[2]/p[1]/i[3]/text())[2])").extract_first()
        time_format=response.xpath("normalize-space((/html/body/section/div/div/div[2]/div[2]/p[1]/i[4]/text())[2])").extract_first()
        refree=response.xpath("normalize-space(/html/body/section/div/div/div[2]/div[2]/p[1]/i[5]/span/text())").extract_first()
        details=response.xpath("normalize-space((/html/body/section/div/div/div[2]/div[2]/p[2]/text())[2])").extract_first()
        if details =='':
            try:
                names=response.xpath("/html/body/section/div/div/div[2]/div[2]/p[2]/i/span/text()").extract()
                value_list=[]
                values=response.xpath("/html/body/section/div/div/div[2]/div[2]/p[2]/i[@class='b-fight-details__text-item']/text()").extract()
                for val in values:
                    value=val.strip()
                    value_list.append(value)
                details=names[0]+' '+value_list[1]+' '+names[1]+' '+value_list[3]+' '+names[2]+' '+value_list[5]
            except:
                details=response.xpath("/html/body/section/div/div/div[2]/div[2]/p[2]/i[@class='b-fight-details__text-item']//text()").extract()
        else:
            pass

        fighter1=response.xpath("((//tr[@class='b-fight-details__table-row'])[2]//p[@class='b-fight-details__table-text']/a)[1]/text()").extract_first()
        fighter2=response.xpath("((//tr[@class='b-fight-details__table-row'])[2]//p[@class='b-fight-details__table-text']/a)[2]/text()").extract_first()
        kd1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[1]/text())").extract_first()
        kd2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[2]/text())").extract_first()
        sig_str1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[3]/text())").extract_first()
        sig_str2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[4]/text())").extract_first()
        sig_str_percent1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[5]/text())").extract_first()
        sig_str_percent2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[6]/text())").extract_first()
        total_str1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[7]/text())").extract_first()
        total_str2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[8]/text())").extract_first()
        td1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[9]/text())").extract_first()
        td2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[10]/text())").extract_first()
        td_percent1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[11]/text())").extract_first()
        td_percent2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[12]/text())").extract_first()
        sub_att1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[13]/text())").extract_first()
        sub_att2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[14]/text())").extract_first()
        rev1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[15]/text())").extract_first()
        rev2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[16]/text())").extract_first()
        ctrl1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[17]/text())").extract_first()
        ctrl2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[2]//td[@class='b-fight-details__table-col']/p)[18]/text())").extract_first()
        head1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[5]/text())").extract_first()
        head2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[6]/text())").extract_first()
        body1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[7]/text())").extract_first()
        body2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[8]/text())").extract_first()
        leg1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[9]/text())").extract_first()
        leg2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[10]/text())").extract_first()
        distance1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[11]/text())").extract_first()
        distance2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[12]/text())").extract_first()
        clinch1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[13]/text())").extract_first()
        clinch2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[14]/text())").extract_first()
        ground1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[15]/text())").extract_first()
        ground2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[8]//td[@class='b-fight-details__table-col']/p)[16]/text())").extract_first()
        if head1:
            pass
        else:
            head1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[5]/text())").extract_first()
            head2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[6]/text())").extract_first()
            body1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[7]/text())").extract_first()
            body2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[8]/text())").extract_first()
            leg1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[9]/text())").extract_first()
            leg2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[10]/text())").extract_first()
            distance1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[11]/text())").extract_first()
            distance2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[12]/text())").extract_first()
            clinch1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[13]/text())").extract_first()
            clinch2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[14]/text())").extract_first()
            ground1=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[15]/text())").extract_first()
            ground2=response.xpath("normalize-space(((//tr[@class='b-fight-details__table-row'])[7]//td[@class='b-fight-details__table-col']/p)[16]/text())").extract_first()

        try:
            sig_str1=sig_str1.split(' of ')
            landed_sig_str1=sig_str1[0]
            attempted_sig_str1=sig_str1[1]
        except:
            landed_sig_str1=sig_str1
            attempted_sig_str1=sig_str1

        try:
            sig_str2=sig_str2.split(' of ')
            landed_sig_str2=sig_str2[0]
            attempted_sig_str2=sig_str2[1]
        except:
            landed_sig_str2=sig_str2
            attempted_sig_str2=sig_str2
            
        try:
            td1=td1.split(' of ')
            landed_td1=td1[0]
            attempted_td1=td1[1]
        except:
            landed_td1=td1
            attempted_td1=td1
        try:
            td2=td2.split(' of ')
            landed_td2=td2[0]
            attempted_td2=td2[1]
        except:
            landed_td2=td2
            attempted_td2=td2




        yield{
            'Title':fight_title,
            'Loser':loser,
            'Winner':winner,
            'Weight_Class':weight_class,
            'Method':method,
            'Rounds':rnds,
            'Time':time,
            'Time Format':time_format,
            'Refree':refree,
            'Details':details,
            'Fighter(A)':fighter1,
            'KnockDowns(A)':kd1,
            'LANDED SIG. STR(A)':landed_sig_str1,
            'ATTEMPTED SIG. STR(A)':attempted_sig_str1,
            'SIG. STR%(A)':sig_str_percent1,
            'TOTAL STR(A)':total_str1,
            'LANDED_TD(A)':landed_td1,
            'ATTEMPTED_TD(A)':attempted_td1,
            'TD% (A)':td_percent1,
            'SUB_ATT(A)':sub_att1,
            'REV(A)':rev1,
            'CTRL(A)':ctrl1,
            'HEAD(A)':head1,
            'BODY(A)':body1,
            'LEG(A)':leg1,
            'DISTANCE(A)':distance1,
            'CLINCH(A)':clinch1,
            'GROUND(A)':ground1,
            'Fighter(B)':fighter2,
            'KnockDowns(B)':kd2,
            'LANDED SIG. STR(B)':landed_sig_str2,
            'ATTEMPTED SIG. STR(B)':attempted_sig_str2,
            'SIG. STR%(B)':sig_str_percent2,
            'TOTAL STR(B)':total_str2,
            'LANDED_TD(B)':landed_td2,
            'ATTEMPTED_TD(B)':attempted_td2,
            'TD% (B)':td_percent2,
            'SUB_ATT(B)':sub_att2,
            'REV(B)':rev2,
            'CTRL(B)':ctrl2,
            'HEAD(B)':head2,
            'BODY(B)':body2,
            'LEG(B)':leg2,
            'DISTANCE(B)':distance2,
            'CLINCH(B)':clinch2,
            'GROUND(B)':ground2,

        }



        