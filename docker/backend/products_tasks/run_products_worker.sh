#!/bin/bash
celery -A core worker -l info -Q products_tasks