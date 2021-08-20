#!/bin/bash
celery -A core worker -l info -Q categories_tasks