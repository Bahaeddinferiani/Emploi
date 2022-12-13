from odoo import models, fields

class postes(models.Model):
    _name = 'publication.postes'
    _description = 'publication.publication'
    Config = fields.Char(string="Titre De recherche",required=True)
    Nom = fields.Char(string="Poste")
    Lien = fields.Char(string="Lien")
    Publicateur = fields.Char(string="publicateur")
    desc = fields.Char(string="Description")
    datepub = fields.Char(string="Date publication")



