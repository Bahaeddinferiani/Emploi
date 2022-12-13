from odoo import models, fields, api
import requests
from bs4 import BeautifulSoup
from lxml import etree as et

class Config(models.Model):
    _name = 'publication.config'
    _description = 'publication.config'
    Config = fields.Char(string="Titre a rechercher",required=True)
    Region = fields.Selection(string="Region", selection=[('Toute la tunisie','Toute la tunisie'), ('bizerte','bizerte'), ('ariana', 'ariana'), ('manouba', 'manouba')])

    @api.model
    def create(self, vals_list):
        stores = self.env['publication.postes'].search([])
        start_url = "https://www.offre-emploi.tn/?s=" + vals_list["Config"]+"&region="+str(vals_list["Region"])
        if(vals_list["Region"] == 'Toute la tunisie'):
            start_url = "https://www.offre-emploi.tn/?s=" + vals_list["Config"] + "&region="

        print(start_url)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        response = requests.get(start_url, headers=header)
        chorba = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(chorba))
        nom = dom.xpath('//a[@rel="bookmark"]/span/text()')
        lien = dom.xpath('//a[@rel="bookmark"]/@href')
        description = dom.xpath('//div[@class="preview"]/text()')
        date = dom.xpath("//time/text()")
        for i in range(len(nom)):
            re = {'Nom': nom[i], 'Lien': lien[i], 'Publicateur': 'Emploi.tn', 'desc': description[i],
                  'datepub': date[i], 'Config': vals_list["Config"]}
            self.env['publication.postes'].create(re)
        self.env.cr.commit()

        return super(Config, self).create(vals_list)