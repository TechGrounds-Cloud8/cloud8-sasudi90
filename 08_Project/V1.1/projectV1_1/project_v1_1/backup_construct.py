from aws_cdk import(
    aws_backup as backup,
    aws_events as event,
    RemovalPolicy,
    Duration,
)

from constructs import Construct

class Backup_construct(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id)

        self.back_up_vault = backup.BackupVault(
            self, "backup_vault",
            backup_vault_name="backup_vault",
            removal_policy=RemovalPolicy.DESTROY,
        )

        self.backup_plan=backup.BackupPlan(
            self, 
            "backup_webserver",
            backup_plan_name="backup_webserver",
            backup_vault=self.back_up_vault,        
        )

        self.backup_plan.add_rule(
            rule=backup.BackupPlanRule(
                rule_name="daily_backup_webserver",
                delete_after=Duration.days(7),
                enable_continuous_backup=True,
                schedule_expression=event.Schedule.cron(
                    minute="0",
                    hour="3",
                )
            )
        )