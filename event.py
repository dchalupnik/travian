from datetime import date

from sqlalchemy import event
from models import RulesRead

@event.listen(RulesRead, 'before_insert')
def update_created_modified_on_create_listener(mapper, connection, target):
  """ Event listener that runs before a record is updated, and sets the create/modified field accordingly."""
  target.date = date.now()

@event.listen(RulesRead, 'before_update')
def update_modified_on_update_listener(mapper, connection, target):
  """ Event listener that runs before a record is updated, and sets the modified field accordingly."""
  # it's okay if this field doesn't exist - SQLAlchemy will silently ignore it.
  target.date = date.now()