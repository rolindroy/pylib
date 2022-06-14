from pulumi_aws import ec2

def build_vpc(cidr, name):
    vpc = ec2.Vpc(
    'eks-vpc',
    cidr_block=cidr,
    tags={
        'Name': name,
        'Test': 'Tag2'
    },
)