from odoo import http
from odoo.http import request
import random


class WebsiteController(http.Controller):

    @http.route('/job_portal', type='http', auth='public', website=True)
    def hr_job_history(self):
        pass_jobs = request.env['hr.job'].sudo().search([('state', '=', 'recruit')])
        job_ids = [job.id for job in pass_jobs]
        diff_jobs = []
        for i in range(4):
            rand_jobs = random.choices(job_ids)
            diff_jobs.append(rand_jobs[0])
            job_ids.remove(rand_jobs[0])

        all_jobs = request.env['hr.job'].sudo().search([('id', 'in', diff_jobs)])
        vals = {"all_jobs": all_jobs, 'page_name': 'Home'}
        return request.render('dynamic_snippet.jobs_snippet', vals)

    @http.route('/job/<int:job_id>', type='http', auth='public', website=True)
    def hor_job(self, job_id=None):
        one_job = request.env['hr.job'].sudo().search([('id', '=', job_id)])
        vals = {"one_job": one_job}
        return request.render('dynamic_snippet.job_particular', vals)

    @http.route(['/get_jobs'], type='json', auth="public", website=True)
    def get_jobs(self, limit=4):
        c = []
        pass_jobs = request.env['hr.job'].sudo().search([('state', '=', 'recruit')])
        job_ids = [job.id for job in pass_jobs]
        diff_jobs = []
        for i in range(limit):
            rand_jobs = random.choices(job_ids)
            diff_jobs.append(rand_jobs[0])
            job_ids.remove(rand_jobs[0])

        jobs = request.env['hr.job'].sudo().search([('id', 'in', diff_jobs)])
        for job in jobs:
            news = {
                "name": job.name,
                "id": job.id,
                "description": job.description,
                "department": job.department_id.name
            }
            c.append(news)
        return c
